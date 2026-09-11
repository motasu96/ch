import os
import sys
import json
import time
import queue
import threading
from flask import Flask, render_template, render_template_string, request, jsonify, Response, send_file
from stripe import TypeWhizzStripeChecker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
app = Flask(__name__, template_folder=TEMPLATE_DIR)

EMBEDDED_INDEX_HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TypeWhizz Stripe Checker - Web Dashboard v2</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-primary: #0b0f19;
            --bg-secondary: #111827;
            --bg-card: rgba(17, 24, 39, 0.75);
            --border-color: rgba(255, 255, 255, 0.08);
            --border-hover: rgba(255, 255, 255, 0.2);
            --accent-primary: #6366f1;
            --accent-glow: rgba(99, 102, 241, 0.35);
            --approved-color: #10b981;
            --approved-glow: rgba(16, 185, 129, 0.25);
            --declined-color: #ef4444;
            --declined-glow: rgba(239, 68, 68, 0.25);
            --otp-color: #f59e0b;
            --otp-glow: rgba(245, 158, 11, 0.25);
            --error-color: #a855f7;
            --text-primary: #f9fafb;
            --text-secondary: #9ca3af;
            --font-family: 'Outfit', 'Tajawal', sans-serif;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background-color: var(--bg-primary);
            background-image: 
                radial-gradient(at 15% 15%, rgba(99, 102, 241, 0.15) 0px, transparent 50%),
                radial-gradient(at 85% 85%, rgba(16, 185, 129, 0.12) 0px, transparent 50%);
            color: var(--text-primary);
            font-family: var(--font-family);
            min-height: 100vh;
            padding: 2rem 1rem;
            display: flex;
            justify-content: center;
        }
        .container { width: 100%; max-width: 1240px; display: flex; flex-direction: column; gap: 1.5rem; }
        header {
            background: var(--bg-card);
            backdrop-filter: blur(16px);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 1.25rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }
        .logo-area { display: flex; align-items: center; gap: 1rem; }
        .logo-icon {
            width: 48px; height: 48px;
            background: linear-gradient(135deg, var(--accent-primary), #8b5cf6);
            border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.5rem; color: #fff; box-shadow: 0 0 20px var(--accent-glow);
        }
        .logo-text h1 { font-size: 1.35rem; font-weight: 700; letter-spacing: -0.5px; }
        .logo-text p { font-size: 0.85rem; color: var(--text-secondary); }
        .header-badges { display: flex; align-items: center; gap: 0.75rem; }
        .badge {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            padding: 0.4rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            color: var(--text-secondary);
            display: flex; align-items: center; gap: 0.4rem;
        }
        .badge-live { background: rgba(16, 185, 129, 0.1); border-color: rgba(16, 185, 129, 0.3); color: var(--approved-color); }
        .pulse-dot {
            width: 8px; height: 8px; background-color: var(--approved-color);
            border-radius: 50%; box-shadow: 0 0 10px var(--approved-color);
            animation: pulse 1.8s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; }
        .stat-card {
            background: var(--bg-card); backdrop-filter: blur(12px);
            border: 1px solid var(--border-color); border-radius: 14px; padding: 1.2rem;
            display: flex; flex-direction: column; gap: 0.5rem; transition: all 0.3s ease;
        }
        .stat-card:hover { border-color: var(--border-hover); transform: translateY(-2px); }
        .stat-card.approved { border-left: 4px solid var(--approved-color); }
        .stat-card.declined { border-left: 4px solid var(--declined-color); }
        .stat-card.otp { border-left: 4px solid var(--otp-color); }
        .stat-card.errors { border-left: 4px solid var(--error-color); }
        .stat-title { font-size: 0.85rem; color: var(--text-secondary); display: flex; justify-content: space-between; align-items: center; }
        .stat-value { font-size: 1.8rem; font-weight: 700; }
        .main-layout { display: grid; grid-template-columns: 1fr 1.6fr; gap: 1.5rem; }
        @media (max-width: 900px) { .main-layout { grid-template-columns: 1fr; } }
        .card-box {
            background: var(--bg-card); backdrop-filter: blur(16px);
            border: 1px solid var(--border-color); border-radius: 16px; padding: 1.5rem;
            display: flex; flex-direction: column; gap: 1.2rem;
        }
        .tab-buttons { display: flex; background: rgba(0, 0, 0, 0.3); border-radius: 10px; padding: 4px; gap: 4px; }
        .tab-btn {
            flex: 1; padding: 0.6rem; border: none; background: transparent;
            color: var(--text-secondary); font-family: var(--font-family); font-size: 0.9rem; font-weight: 500;
            border-radius: 8px; cursor: pointer; transition: all 0.2s ease;
            display: flex; align-items: center; justify-content: center; gap: 0.5rem;
        }
        .tab-btn.active { background: var(--accent-primary); color: #fff; box-shadow: 0 4px 12px var(--accent-glow); }
        .tab-content { display: none; flex-direction: column; gap: 1rem; }
        .tab-content.active { display: flex; }
        .form-group { display: flex; flex-direction: column; gap: 0.5rem; }
        label { font-size: 0.85rem; color: var(--text-secondary); font-weight: 500; }
        input[type="text"], textarea, select {
            width: 100%; background: rgba(0, 0, 0, 0.4); border: 1px solid var(--border-color);
            border-radius: 10px; padding: 0.8rem 1rem; color: var(--text-primary);
            font-family: monospace; font-size: 0.95rem; outline: none; transition: border-color 0.2s ease;
        }
        input[type="text"]:focus, textarea:focus { border-color: var(--accent-primary); box-shadow: 0 0 10px var(--accent-glow); }
        textarea { resize: vertical; min-height: 140px; }
        .file-upload-box {
            border: 2px dashed var(--border-color); border-radius: 10px; padding: 1.5rem;
            text-align: center; cursor: pointer; transition: all 0.2s ease; background: rgba(0, 0, 0, 0.2);
        }
        .file-upload-box:hover { border-color: var(--accent-primary); background: rgba(99, 102, 241, 0.05); }
        .file-upload-box i { font-size: 2rem; color: var(--accent-primary); margin-bottom: 0.5rem; }
        .btn {
            background: linear-gradient(135deg, var(--accent-primary), #4f46e5); color: #fff;
            border: none; border-radius: 10px; padding: 0.85rem 1.5rem; font-family: var(--font-family);
            font-size: 0.95rem; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center;
            gap: 0.5rem; transition: all 0.2s ease; box-shadow: 0 4px 14px var(--accent-glow);
        }
        .btn:hover { opacity: 0.95; transform: translateY(-1px); }
        .btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
        .btn-danger { background: linear-gradient(135deg, var(--declined-color), #dc2626); box-shadow: 0 4px 14px var(--declined-glow); }
        .btn-outline { background: transparent; border: 1px solid var(--border-color); box-shadow: none; color: var(--text-secondary); }
        .btn-outline:hover { background: rgba(255, 255, 255, 0.05); color: var(--text-primary); }
        .progress-area { display: flex; flex-direction: column; gap: 0.5rem; }
        .progress-header { display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-secondary); }
        .progress-track { height: 10px; background: rgba(0, 0, 0, 0.4); border-radius: 5px; overflow: hidden; border: 1px solid var(--border-color); }
        .progress-fill { height: 100%; width: 0%; background: linear-gradient(90deg, var(--accent-primary), var(--approved-color)); border-radius: 5px; transition: width 0.3s ease; }
        .terminal-header { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem; }
        .filter-buttons { display: flex; gap: 0.4rem; }
        .filter-btn {
            background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border-color);
            color: var(--text-secondary); padding: 0.3rem 0.6rem; border-radius: 6px; font-size: 0.75rem; cursor: pointer; font-family: var(--font-family);
        }
        .filter-btn.active { background: rgba(255, 255, 255, 0.15); color: var(--text-primary); border-color: var(--border-hover); }
        .results-container { max-height: 480px; overflow-y: auto; display: flex; flex-direction: column; gap: 0.6rem; padding-right: 4px; }
        .result-item {
            background: rgba(0, 0, 0, 0.3); border: 1px solid var(--border-color); border-radius: 10px;
            padding: 0.8rem 1rem; display: flex; justify-content: space-between; align-items: center;
            font-family: monospace; font-size: 0.88rem; gap: 0.5rem; animation: fadeIn 0.3s ease;
        }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: translateY(0); } }
        .result-item.APPROVED { border-right: 4px solid var(--approved-color); }
        .result-item.DECLINED { border-right: 4px solid var(--declined-color); }
        .result-item.OTP_REQUIRED { border-right: 4px solid var(--otp-color); }
        .result-item.ERROR { border-right: 4px solid var(--error-color); }
        .result-badge { padding: 0.25rem 0.6rem; border-radius: 6px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; }
        .badge-approved { background: rgba(16, 185, 129, 0.15); color: var(--approved-color); }
        .badge-declined { background: rgba(239, 68, 68, 0.15); color: var(--declined-color); }
        .badge-otp { background: rgba(245, 158, 11, 0.15); color: var(--otp-color); }
        .badge-error { background: rgba(168, 85, 247, 0.15); color: var(--error-color); }
        .result-card-info { display: flex; flex-direction: column; gap: 0.2rem; flex: 1; }
        .result-msg { font-size: 0.78rem; color: var(--text-secondary); }
        .result-actions { display: flex; gap: 0.4rem; }
        .action-icon { cursor: pointer; color: var(--text-secondary); padding: 0.3rem; border-radius: 4px; transition: color 0.2s ease; }
        .action-icon:hover { color: var(--text-primary); background: rgba(255, 255, 255, 0.1); }
        .export-bar { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 0.6rem; }
        .empty-state { text-align: center; color: var(--text-secondary); padding: 3rem 1rem; font-size: 0.9rem; }
        .empty-state i { font-size: 2.5rem; margin-bottom: 0.8rem; opacity: 0.4; }
    </style>
</head>
<body>
<div class="container">
    <header>
        <div class="logo-area">
            <div class="logo-icon"><i class="fa-solid fa-credit-card"></i></div>
            <div class="logo-text">
                <h1>TypeWhizz Stripe Checker</h1>
                <p>Auto-Register Engine & Setup Intent Flow v2</p>
            </div>
        </div>
        <div class="header-badges">
            <div class="badge badge-live">
                <div class="pulse-dot"></div>
                <span>Server Ready</span>
            </div>
            <div class="badge">
                <i class="fa-solid fa-code"></i>
                <span>@sudo_3 | TEAM SCR</span>
            </div>
        </div>
    </header>
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-title"><span>الإجمالي Processed</span><i class="fa-solid fa-layer-group"></i></div>
            <div class="stat-value" id="stat-total">0</div>
        </div>
        <div class="stat-card approved">
            <div class="stat-title"><span>مقبول Approved</span><i class="fa-solid fa-circle-check" style="color: var(--approved-color)"></i></div>
            <div class="stat-value" style="color: var(--approved-color)" id="stat-approved">0</div>
        </div>
        <div class="stat-card declined">
            <div class="stat-title"><span>مرفوض Declined</span><i class="fa-solid fa-circle-xmark" style="color: var(--declined-color)"></i></div>
            <div class="stat-value" style="color: var(--declined-color)" id="stat-declined">0</div>
        </div>
        <div class="stat-card otp">
            <div class="stat-title"><span>طلب حماية OTP</span><i class="fa-solid fa-shield-halved" style="color: var(--otp-color)"></i></div>
            <div class="stat-value" style="color: var(--otp-color)" id="stat-otp">0</div>
        </div>
        <div class="stat-card errors">
            <div class="stat-title"><span>أخطاء Errors</span><i class="fa-solid fa-triangle-exclamation" style="color: var(--error-color)"></i></div>
            <div class="stat-value" style="color: var(--error-color)" id="stat-errors">0</div>
        </div>
    </div>
    <div class="main-layout">
        <div class="card-box">
            <div class="tab-buttons">
                <button class="tab-btn active" onclick="switchTab('single')"><i class="fa-solid fa-bolt"></i> فحص مفرد</button>
                <button class="tab-btn" onclick="switchTab('mass')"><i class="fa-solid fa-list-check"></i> فحص جملة / ملف</button>
            </div>
            <div id="tab-single" class="tab-content active">
                <div class="form-group">
                    <label>أدخل بيانات البطاقة (format: number|mm|yy|cvv)</label>
                    <input type="text" id="single-card-input" placeholder="4769700688795135|06|29|885">
                </div>
                <button class="btn" id="btn-single-check" onclick="checkSingleCard()"><i class="fa-solid fa-play"></i> فحص الآن</button>
                <div id="single-result-box"></div>
            </div>
            <div id="tab-mass" class="tab-content">
                <div class="form-group">
                    <label>الصق البطاقات هنا (بطاقة في كل سطر)</label>
                    <textarea id="mass-cards-input" placeholder="4769700688795135|06|29|885&#10;4271229726723512|10|33|420"></textarea>
                </div>
                <div class="file-upload-box" onclick="document.getElementById('file-input').click()">
                    <i class="fa-solid fa-file-arrow-up"></i>
                    <p style="font-size: 0.9rem;">اضغط هنا لرفع ملف كومبو (.txt)</p>
                    <span id="file-name" style="font-size: 0.75rem; color: var(--text-secondary);">لم يتم اختيار ملف</span>
                    <input type="file" id="file-input" accept=".txt" style="display: none;" onchange="handleFileUpload(event)">
                </div>
                <div class="form-group">
                    <label>تأخير التأخير بين الفحوصات (بالثواني)</label>
                    <input type="number" id="delay-input" value="4" min="1" max="60" style="padding: 0.6rem 1rem;">
                </div>
                <div style="display: flex; gap: 0.6rem;">
                    <button class="btn" id="btn-start-scan" style="flex: 1;" onclick="startBatchScan()"><i class="fa-solid fa-play"></i> بدء الفحص</button>
                    <button class="btn btn-danger" id="btn-stop-scan" style="display: none;" onclick="stopScan()"><i class="fa-solid fa-stop"></i> إيقاف</button>
                </div>
            </div>
            <div class="progress-area" id="progress-area" style="display: none;">
                <div class="progress-header"><span id="progress-status">جاري الفحص...</span><span id="progress-counter">0 / 0</span></div>
                <div class="progress-track"><div class="progress-fill" id="progress-fill"></div></div>
            </div>
            <div style="display: flex; justify-content: space-between; border-top: 1px solid var(--border-color); padding-top: 0.8rem;">
                <button class="btn btn-outline" style="font-size: 0.8rem; padding: 0.4rem 0.8rem;" onclick="clearLogs()"><i class="fa-solid fa-trash-can"></i> مسح السجلات</button>
            </div>
        </div>
        <div class="card-box">
            <div class="terminal-header">
                <h3 style="font-size: 1.1rem; font-weight: 600;">سجل الفحص المباشر (Live Terminal)</h3>
                <div class="filter-buttons">
                    <button class="filter-btn active" onclick="filterResults('ALL')">الكل</button>
                    <button class="filter-btn" onclick="filterResults('APPROVED')">المقبول</button>
                    <button class="filter-btn" onclick="filterResults('DECLINED')">المرفوض</button>
                    <button class="filter-btn" onclick="filterResults('OTP_REQUIRED')">OTP</button>
                </div>
            </div>
            <div class="results-container" id="results-list">
                <div class="empty-state"><i class="fa-solid fa-terminal"></i><p>في انتظار بدء عملية الفحص...</p></div>
            </div>
            <div style="border-top: 1px solid var(--border-color); padding-top: 1rem;">
                <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 0.6rem;">تنزيل ملفات النتائج:</p>
                <div class="export-bar">
                    <a href="/api/download/approved" class="btn btn-outline" style="font-size: 0.8rem; padding: 0.5rem; text-decoration: none;"><i class="fa-solid fa-download" style="color: var(--approved-color);"></i> المقبول</a>
                    <a href="/api/download/declined" class="btn btn-outline" style="font-size: 0.8rem; padding: 0.5rem; text-decoration: none;"><i class="fa-solid fa-download" style="color: var(--declined-color);"></i> المرفوض</a>
                    <a href="/api/download/otp" class="btn btn-outline" style="font-size: 0.8rem; padding: 0.5rem; text-decoration: none;"><i class="fa-solid fa-download" style="color: var(--otp-color);"></i> OTP</a>
                </div>
            </div>
        </div>
    </div>
</div>
<script>
    let currentFilter = 'ALL'; let resultsData = []; let eventSource = null;
    function switchTab(tab) {
        document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        if (tab === 'single') {
            document.querySelectorAll('.tab-btn')[0].classList.add('active');
            document.getElementById('tab-single').classList.add('active');
        } else {
            document.querySelectorAll('.tab-btn')[1].classList.add('active');
            document.getElementById('tab-mass').classList.add('active');
        }
    }
    function handleFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
            document.getElementById('file-name').innerText = file.name;
            const reader = new FileReader();
            reader.onload = function(e) { document.getElementById('mass-cards-input').value = e.target.result; };
            reader.readAsText(file);
        }
    }
    async function checkSingleCard() {
        const input = document.getElementById('single-card-input');
        const card = input.value.trim();
        const btn = document.getElementById('btn-single-check');
        const box = document.getElementById('single-result-box');
        if (!card) return alert('الرجاء إدخال بيانات البطاقة');
        btn.disabled = true; btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> جاري الفحص...`; box.innerHTML = '';
        try {
            const resp = await fetch('/api/check-single', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({card: card}) });
            const data = await resp.json();
            if (data.success) { addResultToUI(data.result); updateStatsFromSingle(data.result.status); }
        } catch (e) { alert('حدث خطأ أثناء الاتصال بالخادم: ' + e); }
        finally { btn.disabled = false; btn.innerHTML = `<i class="fa-solid fa-play"></i> فحص الآن`; }
    }
    async function startBatchScan() {
        const text = document.getElementById('mass-cards-input').value.trim();
        if (!text) return alert('الرجاء إدخال بطاقات أو رفع ملف أولاً');
        const cards = text.split('\\n').map(c => c.trim()).filter(c => c);
        const delay = parseFloat(document.getElementById('delay-input').value) || 4;
        const btnStart = document.getElementById('btn-start-scan'); const btnStop = document.getElementById('btn-stop-scan');
        const progressArea = document.getElementById('progress-area');
        btnStart.style.display = 'none'; btnStop.style.display = 'flex'; progressArea.style.display = 'flex';
        connectSSE();
        try {
            const resp = await fetch('/api/start-scan', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({cards: cards, delay: delay}) });
            const data = await resp.json();
            if (!data.success) { alert(data.message); btnStart.style.display = 'flex'; btnStop.style.display = 'none'; }
        } catch (e) { alert('خطأ في بدء الفحص: ' + e); }
    }
    async function stopScan() { await fetch('/api/stop-scan', {method: 'POST'}); }
    function connectSSE() {
        if (eventSource) eventSource.close();
        eventSource = new EventSource('/api/stream');
        eventSource.onmessage = function(event) {
            const data = JSON.parse(event.data);
            if (data.type === 'item') { addResultToUI(data.result); updateStats(data.stats, data.index, data.total); }
            else if (data.type === 'finished' || data.type === 'stopped') {
                eventSource.close(); document.getElementById('btn-start-scan').style.display = 'flex';
                document.getElementById('btn-stop-scan').style.display = 'none';
                document.getElementById('progress-status').innerText = data.type === 'finished' ? 'اكتمل الفحص!' : 'تم الإيقاف';
            }
        };
    }
    function addResultToUI(res) {
        const list = document.getElementById('results-list'); const emptyState = list.querySelector('.empty-state');
        if (emptyState) emptyState.remove();
        resultsData.unshift(res);
        const statusClass = res.status || 'ERROR';
        const badgeText = {'APPROVED':'APPROVED', 'DECLINED':'DECLINED', 'OTP_REQUIRED':'OTP 3DS', 'ERROR':'ERROR'}[statusClass] || statusClass;
        const badgeClass = {'APPROVED':'badge-approved', 'DECLINED':'badge-declined', 'OTP_REQUIRED':'badge-otp', 'ERROR':'badge-error'}[statusClass] || 'badge-error';
        const item = document.createElement('div'); item.className = `result-item ${statusClass}`; item.setAttribute('data-status', statusClass);
        item.innerHTML = `
            <span class="result-badge ${badgeClass}">${badgeText}</span>
            <div class="result-card-info"><span>${res.card}</span><span class="result-msg">${res.message || ''}</span></div>
            <div class="result-actions"><i class="fa-regular fa-copy action-icon" onclick="copyCard('${res.card}')" title="نسخ البطاقة"></i></div>
        `;
        if (currentFilter !== 'ALL' && currentFilter !== statusClass) item.style.display = 'none';
        list.prepend(item);
    }
    function updateStats(stats, current, total) {
        document.getElementById('stat-total').innerText = current;
        document.getElementById('stat-approved').innerText = stats.approved;
        document.getElementById('stat-declined').innerText = stats.declined;
        document.getElementById('stat-otp').innerText = stats.otp;
        document.getElementById('stat-errors').innerText = stats.errors;
        const pct = Math.round((current / total) * 100);
        document.getElementById('progress-fill').style.width = pct + '%';
        document.getElementById('progress-counter').innerText = `${current} / ${total} (${pct}%)`;
    }
    function updateStatsFromSingle(status) {
        const totalEl = document.getElementById('stat-total'); totalEl.innerText = parseInt(totalEl.innerText || 0) + 1;
        if (status === 'APPROVED') { const el = document.getElementById('stat-approved'); el.innerText = parseInt(el.innerText || 0) + 1; }
        else if (status === 'DECLINED') { const el = document.getElementById('stat-declined'); el.innerText = parseInt(el.innerText || 0) + 1; }
        else if (status === 'OTP_REQUIRED') { const el = document.getElementById('stat-otp'); el.innerText = parseInt(el.innerText || 0) + 1; }
        else { const el = document.getElementById('stat-errors'); el.innerText = parseInt(el.innerText || 0) + 1; }
    }
    function filterResults(type) {
        currentFilter = type; document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active')); event.target.classList.add('active');
        document.querySelectorAll('.result-item').forEach(item => { item.style.display = (type === 'ALL' || item.getAttribute('data-status') === type) ? 'flex' : 'none'; });
    }
    function copyCard(text) { navigator.clipboard.writeText(text); alert('تم نسخ البطاقة: ' + text); }
    async function clearLogs() {
        if (confirm('هل أنت تأكد من مسح جميع السجلات والملفات؟')) {
            await fetch('/api/clear-logs', {method: 'POST'});
            document.getElementById('results-list').innerHTML = `<div class="empty-state"><i class="fa-solid fa-terminal"></i><p>تم مسح السجلات.</p></div>`;
            document.getElementById('stat-total').innerText = '0'; document.getElementById('stat-approved').innerText = '0';
            document.getElementById('stat-declined').innerText = '0'; document.getElementById('stat-otp').innerText = '0'; document.getElementById('stat-errors').innerText = '0';
        }
    }
</script>
</body>
</html>"""

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
    except Exception:
        index_path = os.path.join(TEMPLATE_DIR, 'index.html')
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
        return render_template_string(EMBEDDED_INDEX_HTML)

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
