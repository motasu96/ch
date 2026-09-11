import os
import sys
import json
import time
import queue
import threading
from flask import Flask, render_template, request, jsonify, Response, send_file
from stripe import TypeWhizzStripeChecker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
app = Flask(__name__, template_folder=TEMPLATE_DIR)

# Global Scan State Manager
class ScanManager:
    def __init__(self):
        self.lock = threading.Lock()
        self.is_running = False
        self.stop_requested = False
        self.event_queue = queue.Queue()
        self.current_index = 0
        self.total = 0
        self.delay = 4
        self.stats = {'approved': 0, 'declined': 0, 'otp': 0, 'errors': 0}
        self.thread = None

    def start_scan(self, cards, delay=4):
        with self.lock:
            if self.is_running:
                return False, "Scan is already in progress"
            self.is_running = True
            self.stop_requested = False
            self.current_index = 0
            self.total = len(cards)
            self.delay = delay
            self.stats = {'approved': 0, 'declined': 0, 'otp': 0, 'errors': 0}
            # Clear event queue
            while not self.event_queue.empty():
                try:
                    self.event_queue.get_nowait()
                except queue.Empty:
                    break

            self.thread = threading.Thread(target=self._run_scan_thread, args=(cards,), daemon=True)
            self.thread.start()
            return True, "Scan started"

    def stop_scan(self):
        with self.lock:
            if self.is_running:
                self.stop_requested = True
                return True, "Stop signal sent"
            return False, "No active scan running"

    def _run_scan_thread(self, cards):
        checker = TypeWhizzStripeChecker()
        
        self.event_queue.put({
            'type': 'start',
            'total': self.total,
            'message': f'Scan started for {self.total} cards'
        })

        for i, card in enumerate(cards, 1):
            if self.stop_requested:
                self.event_queue.put({
                    'type': 'stopped',
                    'message': 'Scan stopped by user'
                })
                break

            self.current_index = i
            result = checker.check_card(card)
            
            # Save results to text files
            status = result.get('status', 'ERROR')
            msg = result.get('message', '')
            formatted_card = result.get('card', card)

            if status == 'APPROVED':
                self.stats['approved'] += 1
                with open('approved.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{formatted_card} | {msg}\n")
            elif status == 'DECLINED':
                self.stats['declined'] += 1
                with open('declined.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{formatted_card} | {msg}\n")
            elif status == 'OTP_REQUIRED':
                self.stats['otp'] += 1
                with open('otp.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{formatted_card} | {msg}\n")
            else:
                self.stats['errors'] += 1
                with open('errors.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{formatted_card} | {msg}\n")

            self.event_queue.put({
                'type': 'item',
                'index': i,
                'total': self.total,
                'result': result,
                'stats': self.stats.copy()
            })

            # Delay before next card if not stopped and not last item
            if i < self.total and not self.stop_requested:
                time.sleep(self.delay)

        with self.lock:
            self.is_running = False

        self.event_queue.put({
            'type': 'finished',
            'stats': self.stats.copy(),
            'message': 'Scan completed'
        })

scan_manager = ScanManager()

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        index_path = os.path.join(TEMPLATE_DIR, 'index.html')
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
        return f"Template Error: {str(e)}", 500

@app.route('/api/check-single', methods=['POST'])
def check_single():
    data = request.get_json() or {}
    card = data.get('card', '').strip()
    if not card:
        return jsonify({'success': False, 'message': 'No card provided'}), 400

    checker = TypeWhizzStripeChecker()
    result = checker.check_card(card)

    status = result.get('status', 'ERROR')
    msg = result.get('message', '')
    formatted_card = result.get('card', card)

    if status == 'APPROVED':
        with open('approved.txt', 'a', encoding='utf-8') as f:
            f.write(f"{formatted_card} | {msg}\n")
    elif status == 'DECLINED':
        with open('declined.txt', 'a', encoding='utf-8') as f:
            f.write(f"{formatted_card} | {msg}\n")
    elif status == 'OTP_REQUIRED':
        with open('otp.txt', 'a', encoding='utf-8') as f:
            f.write(f"{formatted_card} | {msg}\n")
    else:
        with open('errors.txt', 'a', encoding='utf-8') as f:
            f.write(f"{formatted_card} | {msg}\n")

    return jsonify({'success': True, 'result': result})

@app.route('/api/start-scan', methods=['POST'])
def start_scan():
    data = request.get_json() or {}
    cards = data.get('cards', [])
    delay = float(data.get('delay', 4))

    if not cards:
        return jsonify({'success': False, 'message': 'No cards provided'}), 400

    cards_list = [c.strip() for c in cards if c.strip()]
    if not cards_list:
        return jsonify({'success': False, 'message': 'No valid cards provided'}), 400

    success, msg = scan_manager.start_scan(cards_list, delay=delay)
    return jsonify({'success': success, 'message': msg, 'total': len(cards_list)})

@app.route('/api/stop-scan', methods=['POST'])
def stop_scan():
    success, msg = scan_manager.stop_scan()
    return jsonify({'success': success, 'message': msg})

@app.route('/api/stream')
def stream_events():
    def event_generator():
        while True:
            try:
                data = scan_manager.event_queue.get(timeout=20)
                yield f"data: {json.dumps(data)}\n\n"
                if data.get('type') in ('finished', 'stopped'):
                    break
            except queue.Empty:
                yield f"data: {json.dumps({'type': 'ping'})}\n\n"

    return Response(event_generator(), mimetype='text/event-stream')

@app.route('/api/download/<result_type>')
def download_results(result_type):
    filename_map = {
        'approved': 'approved.txt',
        'declined': 'declined.txt',
        'otp': 'otp.txt',
        'errors': 'errors.txt'
    }
    target_file = filename_map.get(result_type)
    if not target_file:
        return jsonify({'error': 'Invalid file type'}), 400

    if not os.path.exists(target_file):
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write("")

    return send_file(target_file, as_attachment=True)

@app.route('/api/clear-logs', methods=['POST'])
def clear_logs():
    for fname in ['approved.txt', 'declined.txt', 'otp.txt', 'errors.txt']:
        if os.path.exists(fname):
            with open(fname, 'w', encoding='utf-8') as f:
                f.write("")
    return jsonify({'success': True, 'message': 'Logs cleared successfully'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
