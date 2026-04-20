"""
Nivesh Mitra AI — Reusable UI Components  v2.0
Premium Glassmorphic Fintech UI for Streamlit
"""

import html
import streamlit as st


# ─────────────────────────────────────────────────────────────
#  GLOBAL CSS INJECTION
# ─────────────────────────────────────────────────────────────

def inject_global_css():
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

    <style>
    /* ═══════════════════════════════════════════════════
       DESIGN TOKENS
    ═══════════════════════════════════════════════════ */
    :root {
        /* Background layers */
        --bg-base:        #060A12;
        --bg-deep:        #080D18;
        --bg-mid:         #0B1220;
        --bg-glass:       rgba(13, 20, 38, 0.72);
        --bg-glass-light: rgba(20, 30, 55, 0.60);
        --bg-glass-card:  rgba(16, 25, 46, 0.80);

        /* Brand palette */
        --navy-900: #060A12;
        --navy-800: #0B1525;
        --navy-700: #111E35;
        --purple-600: #5B3FD9;
        --purple-500: #7C5CE8;
        --purple-400: #9D7FF0;
        --blue-600:  #1B5BE3;
        --blue-500:  #2D6EF5;
        --blue-400:  #5B91FF;
        --blue-300:  #8AB4FF;
        --teal-500:  #0DB4B4;
        --teal-400:  #2ECFCF;
        --green-600: #059669;
        --green-500: #10B981;
        --green-400: #34D399;
        --green-300: #6EE7B7;
        --amber-500: #F59E0B;
        --amber-400: #FBBF24;
        --red-500:   #EF4444;

        /* Text */
        --text-primary:   #EEF2FF;
        --text-secondary: #94A3B8;
        --text-muted:     #475569;
        --text-hint:      #334155;

        /* Borders */
        --border:        rgba(99, 130, 200, 0.12);
        --border-glass:  rgba(120, 150, 220, 0.18);
        --border-glow:   rgba(91, 145, 255, 0.35);
        --border-green:  rgba(52, 211, 153, 0.35);
        --border-purple: rgba(124, 92, 232, 0.35);

        /* Typography */
        --font:      'Plus Jakarta Sans', sans-serif;
        --font-mono: 'JetBrains Mono', monospace;

        /* Radii */
        --r-sm: 8px;
        --r-md: 14px;
        --r-lg: 20px;
        --r-xl: 28px;
        --r-2xl: 36px;

        /* Shadows */
        --shadow-base:   0 2px 16px rgba(0,0,0,0.5);
        --shadow-card:   0 8px 40px rgba(0,0,0,0.55), 0 2px 8px rgba(0,0,0,0.4);
        --shadow-float:  0 20px 60px rgba(0,0,0,0.6), 0 4px 16px rgba(0,0,0,0.4);
        --shadow-blue:   0 0 40px rgba(45,110,245,0.18), 0 0 80px rgba(45,110,245,0.08);
        --shadow-green:  0 0 40px rgba(16,185,129,0.18), 0 0 80px rgba(16,185,129,0.08);
        --shadow-purple: 0 0 40px rgba(91,63,217,0.18), 0 0 80px rgba(91,63,217,0.08);
        --shadow-cta:    0 12px 40px rgba(16,185,129,0.35), 0 4px 16px rgba(0,0,0,0.4);

        /* Motion */
        --ease:  cubic-bezier(0.4, 0, 0.2, 1);
        --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
        --t-fast: 0.15s;
        --t-mid:  0.25s;
        --t-slow: 0.4s;
    }

    /* ═══════════════════════════════════════════════════
       GLOBAL RESET + AMBIENT BACKGROUND
    ═══════════════════════════════════════════════════ */
    html, body, [class*="css"], [class*="st-"] {
        font-family: var(--font) !important;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
    }

    /* The magic ambient background */
    .stApp {
        background: var(--bg-base) !important;
        background-image:
            /* Top-left purple nebula */
            radial-gradient(ellipse 70% 55% at 0% 0%,
                rgba(91, 63, 217, 0.22) 0%, transparent 60%),
            /* Center-right blue bloom */
            radial-gradient(ellipse 60% 50% at 100% 30%,
                rgba(29, 91, 227, 0.18) 0%, transparent 60%),
            /* Bottom-left teal whisper */
            radial-gradient(ellipse 50% 40% at 15% 100%,
                rgba(13, 180, 180, 0.12) 0%, transparent 55%),
            /* Bottom-right deep glow */
            radial-gradient(ellipse 55% 45% at 90% 95%,
                rgba(91, 63, 217, 0.14) 0%, transparent 55%)
        !important;
        min-height: 100vh;
    }

    /* Fine grain texture overlay */
    .stApp::before {
        content: '';
        position: fixed;
        inset: 0;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
        pointer-events: none;
        z-index: 0;
        opacity: 0.6;
    }

    /* ── STREAMLIT CHROME CLEANUP ── */
    #MainMenu, footer, header { visibility: hidden !important; }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    section[data-testid="stSidebar"] { display: none !important; }

    /* ═══════════════════════════════════════════════════
       SCROLLBAR
    ═══════════════════════════════════════════════════ */
    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
        background: rgba(91,145,255,0.25);
        border-radius: 99px;
    }

    /* ═══════════════════════════════════════════════════
       WIDGET OVERRIDES — STREAMLIT
    ═══════════════════════════════════════════════════ */
    div[data-testid="stSelectbox"] > div > div {
        background: var(--bg-glass-card) !important;
        border: 1px solid var(--border-glass) !important;
        border-radius: var(--r-md) !important;
        color: var(--text-primary) !important;
        font-family: var(--font) !important;
        font-size: 14px !important;
        backdrop-filter: blur(12px) !important;
    }
    div[data-testid="stTextInput"] > div > div > input {
        background: var(--bg-glass-card) !important;
        border: 1px solid var(--border-glass) !important;
        border-radius: var(--r-lg) !important;
        color: var(--text-primary) !important;
        font-family: var(--font) !important;
        font-size: 15px !important;
        padding: 16px 22px !important;
        transition: border-color var(--t-mid) var(--ease),
                    box-shadow var(--t-mid) var(--ease) !important;
        backdrop-filter: blur(12px) !important;
    }
    div[data-testid="stTextInput"] > div > div > input:focus {
        border-color: var(--blue-500) !important;
        box-shadow: 0 0 0 3px rgba(45,110,245,0.18),
                    0 0 20px rgba(45,110,245,0.12) !important;
        outline: none !important;
    }
    div[data-testid="stTextInput"] > div > div > input::placeholder {
        color: var(--text-muted) !important;
    }
    div.stButton > button {
        font-family: var(--font) !important;
        font-weight: 700 !important;
        border-radius: var(--r-md) !important;
        border: none !important;
        transition: all var(--t-mid) var(--ease) !important;
        letter-spacing: -0.01em !important;
    }

    /* ═══════════════════════════════════════════════════
       HEADER
    ═══════════════════════════════════════════════════ */
    .nm-header {
        text-align: center;
        padding: 64px 32px 48px;
        position: relative;
        overflow: hidden;
        border-bottom: 1px solid var(--border-glass);
    }

    /* Animated orbs behind header */
    .nm-header::before {
        content: '';
        position: absolute;
        width: 600px; height: 600px;
        background: radial-gradient(circle,
            rgba(91,63,217,0.16) 0%,
            rgba(45,110,245,0.10) 40%,
            transparent 70%);
        top: -200px; left: 50%;
        transform: translateX(-50%);
        border-radius: 50%;
        pointer-events: none;
        animation: halo-breathe 6s ease-in-out infinite;
    }
    .nm-header::after {
        content: '';
        position: absolute;
        inset: 0;
        background: url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='1' cy='1' r='0.8' fill='rgba(120,150,220,0.08)'/%3E%3C/svg%3E");
        pointer-events: none;
    }
    @keyframes halo-breathe {
        0%, 100% { transform: translateX(-50%) scale(1);   opacity: 1; }
        50%       { transform: translateX(-50%) scale(1.1); opacity: 0.75; }
    }

    .nm-header-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(45,110,245,0.10);
        border: 1px solid rgba(91,145,255,0.28);
        border-radius: 99px;
        padding: 6px 18px;
        font-size: 11px;
        font-weight: 700;
        color: var(--blue-300);
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 24px;
        position: relative;
        backdrop-filter: blur(8px);
    }
    .nm-header-badge .live-dot {
        width: 7px; height: 7px;
        background: var(--green-400);
        border-radius: 50%;
        box-shadow: 0 0 10px var(--green-400), 0 0 20px rgba(52,211,153,0.4);
        animation: live-pulse 1.8s ease-in-out infinite;
    }
    @keyframes live-pulse {
        0%, 100% { opacity: 1;   transform: scale(1);   }
        50%       { opacity: 0.5; transform: scale(1.4); }
    }

    .nm-title {
        font-size: clamp(36px, 5.5vw, 58px);
        font-weight: 800;
        letter-spacing: -0.04em;
        line-height: 1.05;
        margin: 0 0 18px;
        position: relative;
        background: linear-gradient(
            135deg,
            #FFFFFF      0%,
            #C4D4FF     25%,
            var(--blue-400)  50%,
            var(--teal-400)  75%,
            var(--green-300) 100%
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 0 30px rgba(91,145,255,0.25));
    }
    .nm-tagline {
        font-size: 16px;
        color: var(--text-secondary);
        font-weight: 400;
        max-width: 520px;
        margin: 0 auto;
        line-height: 1.7;
        position: relative;
    }

    /* ── Step indicator chips ── */
    .nm-steps-row {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0;
        margin-top: 36px;
        position: relative;
    }
    .nm-step {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px 20px;
        border-radius: 99px;
        font-size: 13px;
        font-weight: 600;
        color: var(--text-muted);
        transition: all var(--t-mid) var(--ease);
        white-space: nowrap;
    }
    .nm-step.active {
        background: rgba(45,110,245,0.12);
        border: 1px solid rgba(91,145,255,0.3);
        color: var(--blue-300);
    }
    .nm-step.done {
        color: var(--green-400);
    }
    .nm-step-num {
        width: 22px; height: 22px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 11px;
        font-weight: 800;
        background: var(--bg-glass-card);
        border: 1px solid var(--border-glass);
        flex-shrink: 0;
    }
    .nm-step.active .nm-step-num {
        background: var(--blue-500);
        border-color: transparent;
        color: white;
        box-shadow: 0 0 12px rgba(45,110,245,0.5);
    }
    .nm-step.done .nm-step-num {
        background: var(--green-500);
        border-color: transparent;
        color: white;
    }
    .nm-step-line {
        width: 32px; height: 1px;
        background: var(--border-glass);
    }

    /* ═══════════════════════════════════════════════════
       CONTROL BAR
    ═══════════════════════════════════════════════════ */
    .nm-control-bar {
        position: sticky;
        top: 0;
        z-index: 200;
        background: rgba(6, 10, 18, 0.85);
        backdrop-filter: blur(20px) saturate(1.4);
        border-bottom: 1px solid var(--border-glass);
        padding: 14px 32px;
    }

    /* ═══════════════════════════════════════════════════
       CHAT AREA
    ═══════════════════════════════════════════════════ */
    .nm-chat-wrapper {
        max-width: 800px;
        margin: 0 auto;
        padding: 36px 28px 16px;
        display: flex;
        flex-direction: column;
        gap: 4px;
    }

    .nm-chat-row {
        display: flex;
        width: 100%;
        animation: msg-in var(--t-slow) var(--ease) both;
    }
    @keyframes msg-in {
        from { opacity: 0; transform: translateY(12px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    .nm-chat-row.user { justify-content: flex-end; }
    .nm-chat-row.bot  { justify-content: flex-start; }

    /* Avatars */
    .nm-avatar {
        width: 36px; height: 36px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 17px;
        flex-shrink: 0;
        align-self: flex-end;
    }
    .nm-avatar.bot {
        background: linear-gradient(135deg, var(--purple-500), var(--blue-500), var(--teal-500));
        margin-right: 10px;
        box-shadow: 0 0 16px rgba(91,63,217,0.4);
    }
    .nm-avatar.user {
        background: rgba(45,110,245,0.12);
        border: 1px solid rgba(91,145,255,0.3);
        margin-left: 10px;
    }

    /* Bubbles */
    .nm-bubble-wrap { display: flex; flex-direction: column; max-width: 74%; }

    .nm-bubble {
        padding: 14px 20px;
        border-radius: var(--r-lg);
        font-size: 14.5px;
        line-height: 1.7;
        word-break: break-word;
        backdrop-filter: blur(8px);
        transition: transform var(--t-fast) var(--ease);
    }
    .nm-bubble:hover { transform: translateY(-1px); }

    .nm-bubble.user {
        background: linear-gradient(135deg,
            rgba(45,110,245,0.28) 0%,
            rgba(91,63,217,0.18) 100%);
        border: 1px solid rgba(91,145,255,0.28);
        border-bottom-right-radius: 4px;
        color: var(--text-primary);
    }
    .nm-bubble.bot {
        background: var(--bg-glass-card);
        border: 1px solid var(--border-glass);
        border-bottom-left-radius: 4px;
        color: var(--text-primary);
        box-shadow: var(--shadow-base);
    }

    .nm-timestamp {
        font-size: 10.5px;
        color: var(--text-hint);
        font-family: var(--font-mono);
        margin-top: 5px;
        padding: 0 4px;
    }
    .nm-chat-row.user .nm-timestamp { text-align: right; }
    .nm-chat-row.bot  .nm-timestamp { text-align: left;  }

    /* ── Typing indicator ── */
    .nm-typing {
        display: flex;
        align-items: flex-end;
        gap: 10px;
        padding: 4px 28px 20px;
        max-width: 800px;
        margin: 0 auto;
    }
    .nm-typing-dots {
        display: flex;
        gap: 6px;
        background: var(--bg-glass-card);
        border: 1px solid var(--border-glass);
        border-radius: var(--r-lg);
        border-bottom-left-radius: 4px;
        padding: 14px 20px;
        backdrop-filter: blur(8px);
    }
    .nm-typing-dots span {
        width: 7px; height: 7px;
        background: var(--blue-400);
        border-radius: 50%;
        animation: dot-wave 1.3s ease-in-out infinite;
        opacity: 0.5;
    }
    .nm-typing-dots span:nth-child(2) { animation-delay: 0.18s; }
    .nm-typing-dots span:nth-child(3) { animation-delay: 0.36s; }
    @keyframes dot-wave {
        0%, 80%, 100% { transform: translateY(0);   opacity: 0.35; }
        40%            { transform: translateY(-7px); opacity: 1;    }
    }

    /* ── Empty state ── */
    .nm-empty {
        text-align: center;
        padding: 52px 28px;
        max-width: 520px;
        margin: 0 auto;
    }
    .nm-empty-icon {
        font-size: 52px;
        margin-bottom: 20px;
        display: block;
        filter: drop-shadow(0 0 20px rgba(45,110,245,0.3));
    }
    .nm-empty-title {
        font-size: 22px;
        font-weight: 800;
        color: var(--text-primary);
        margin-bottom: 10px;
        letter-spacing: -0.03em;
    }
    .nm-empty-sub {
        font-size: 14.5px;
        color: var(--text-secondary);
        line-height: 1.7;
        margin-bottom: 28px;
    }
    .nm-chips { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; }
    .nm-chip {
        display: inline-block;
        background: var(--bg-glass-card);
        border: 1px solid var(--border-glass);
        border-radius: 99px;
        padding: 8px 18px;
        font-size: 13px;
        font-weight: 500;
        color: var(--text-secondary);
        cursor: pointer;
        transition: all var(--t-mid) var(--ease);
        backdrop-filter: blur(8px);
    }
    .nm-chip:hover {
        border-color: var(--border-glow);
        color: var(--blue-300);
        background: rgba(45,110,245,0.08);
        transform: translateY(-1px);
        box-shadow: 0 4px 16px rgba(45,110,245,0.15);
    }

    /* ═══════════════════════════════════════════════════
       SECTION DIVIDER
    ═══════════════════════════════════════════════════ */
    .nm-section {
        max-width: 800px;
        margin: 28px auto 0;
        padding: 0 28px;
    }
    .nm-section-label {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        color: var(--text-muted);
        margin-bottom: 14px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .nm-section-label::after {
        content: '';
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, var(--border-glass), transparent);
    }

    /* ═══════════════════════════════════════════════════
       HERO RESULT CARD  — THE STAR OF THE SHOW
    ═══════════════════════════════════════════════════ */
    .nm-result-outer {
        max-width: 800px;
        margin: 0 auto 28px;
        padding: 0 28px;
    }
    .nm-result-card {
        position: relative;
        background: var(--bg-glass-card);
        border: 1px solid var(--border-glass);
        border-radius: var(--r-2xl);
        padding: 36px 40px;
        overflow: hidden;
        backdrop-filter: blur(24px);
        box-shadow: var(--shadow-float), var(--shadow-blue);
    }

    /* Gradient top accent bar */
    .nm-result-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg,
            var(--purple-500),
            var(--blue-500),
            var(--teal-400),
            var(--green-400));
        border-radius: var(--r-2xl) var(--r-2xl) 0 0;
    }

    /* Ambient inner glow */
    .nm-result-card::after {
        content: '';
        position: absolute;
        top: -60px; right: -60px;
        width: 240px; height: 240px;
        background: radial-gradient(circle,
            rgba(45,110,245,0.12) 0%, transparent 70%);
        pointer-events: none;
        border-radius: 50%;
    }

    .nm-result-eyebrow {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        color: var(--blue-400);
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .nm-result-eyebrow::before {
        content: '';
        width: 18px; height: 2px;
        background: linear-gradient(90deg, var(--blue-500), var(--teal-400));
        border-radius: 99px;
    }

    .nm-result-headline {
        font-size: 15px;
        font-weight: 600;
        color: var(--text-secondary);
        margin-bottom: 32px;
    }

    /* HERO number — Total Amount */
    .nm-hero-amount-label {
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--text-muted);
        margin-bottom: 6px;
    }
    .nm-hero-amount {
        font-size: clamp(42px, 6vw, 64px);
        font-weight: 800;
        letter-spacing: -0.04em;
        line-height: 1;
        font-family: var(--font-mono);
        background: linear-gradient(135deg,
            var(--green-300) 0%,
            var(--green-400) 50%,
            var(--teal-400) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 0 20px rgba(52,211,153,0.3));
        margin-bottom: 6px;
    }
    .nm-hero-sub {
        font-size: 13px;
        color: var(--green-500);
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 6px;
        margin-bottom: 32px;
    }
    .nm-hero-sub::before {
        content: '↑';
        font-size: 14px;
    }

    /* Metric pills row */
    .nm-metrics-row {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
    }
    .nm-metric-pill {
        flex: 1;
        min-width: 140px;
        background: rgba(6, 10, 18, 0.55);
        border: 1px solid var(--border-glass);
        border-radius: var(--r-lg);
        padding: 20px 22px;
        position: relative;
        overflow: hidden;
        transition: all var(--t-mid) var(--ease);
    }
    .nm-metric-pill:hover {
        border-color: var(--border-glass);
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }
    .nm-metric-pill::before {
        content: '';
        position: absolute;
        inset: 0;
        opacity: 0.04;
        background: linear-gradient(135deg, white, transparent);
    }
    .nm-metric-icon {
        font-size: 22px;
        margin-bottom: 10px;
        display: block;
    }
    .nm-metric-lbl {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--text-muted);
        margin-bottom: 6px;
    }
    .nm-metric-val {
        font-size: 22px;
        font-weight: 800;
        letter-spacing: -0.03em;
        font-family: var(--font-mono);
        line-height: 1;
    }
    .nm-metric-val.blue   { color: var(--blue-400);  }
    .nm-metric-val.amber  { color: var(--amber-400); }
    .nm-metric-val.green  { color: var(--green-400); }
    .nm-metric-note {
        font-size: 11.5px;
        color: var(--text-muted);
        margin-top: 5px;
        font-family: var(--font-mono);
    }

    /* ═══════════════════════════════════════════════════
       COMPARISON CARDS
    ═══════════════════════════════════════════════════ */
    .nm-compare-outer {
        max-width: 800px;
        margin: 0 auto 28px;
        padding: 0 28px;
    }
    .nm-compare-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
    }
    .nm-compare-card {
        background: var(--bg-glass-card);
        border: 1px solid var(--border-glass);
        border-radius: var(--r-xl);
        padding: 28px;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(16px);
        transition: all var(--t-mid) var(--ease);
    }
    .nm-compare-card:hover {
        transform: translateY(-3px);
    }

    /* Winner card — THE best option */
    .nm-compare-card.winner {
        border-color: var(--border-green);
        box-shadow: var(--shadow-green);
        background: rgba(16, 25, 46, 0.90);
    }
    .nm-compare-card.winner::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, var(--green-500), var(--teal-400));
    }
    /* Loser card — dimmed */
    .nm-compare-card.loser {
        opacity: 0.58;
        filter: saturate(0.6);
    }

    /* Best option badge */
    .nm-best-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(16,185,129,0.12);
        border: 1px solid rgba(52,211,153,0.35);
        border-radius: 99px;
        padding: 5px 14px;
        font-size: 11px;
        font-weight: 800;
        color: var(--green-300);
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 16px;
    }
    .nm-bank-name {
        font-size: 19px;
        font-weight: 800;
        color: var(--text-primary);
        letter-spacing: -0.02em;
        margin-bottom: 2px;
    }
    .nm-bank-sub {
        font-size: 12px;
        color: var(--text-muted);
        margin-bottom: 16px;
    }
    .nm-compare-rate {
        font-size: 40px;
        font-weight: 800;
        letter-spacing: -0.04em;
        font-family: var(--font-mono);
        line-height: 1;
        margin-bottom: 4px;
    }
    .nm-compare-rate.green { color: var(--green-400); filter: drop-shadow(0 0 12px rgba(52,211,153,0.3)); }
    .nm-compare-rate.blue  { color: var(--blue-400);  }
    .nm-compare-rate-lbl {
        font-size: 11px;
        color: var(--text-muted);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 18px;
    }
    .nm-compare-stat {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 13px;
        padding: 9px 0;
        border-top: 1px solid var(--border);
        color: var(--text-secondary);
    }
    .nm-compare-stat-val {
        font-weight: 700;
        color: var(--text-primary);
        font-family: var(--font-mono);
        font-size: 13px;
    }
    /* Earn-more callout inside winner card */
    .nm-earn-more {
        margin-top: 18px;
        background: rgba(16,185,129,0.08);
        border: 1px solid rgba(52,211,153,0.2);
        border-radius: var(--r-md);
        padding: 10px 14px;
        font-size: 13px;
        font-weight: 600;
        color: var(--green-300);
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* ═══════════════════════════════════════════════════
       CHART WRAPPER
    ═══════════════════════════════════════════════════ */
    .nm-chart-outer {
        max-width: 800px;
        margin: 0 auto 28px;
        padding: 0 28px;
    }
    .nm-chart-card {
        background: var(--bg-glass-card);
        border: 1px solid var(--border-glass);
        border-radius: var(--r-xl);
        padding: 28px 32px;
        backdrop-filter: blur(16px);
        box-shadow: var(--shadow-card);
    }
    .nm-chart-title {
        font-size: 12px;
        font-weight: 700;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 20px;
    }

    /* ═══════════════════════════════════════════════════
       CTA BUTTON
    ═══════════════════════════════════════════════════ */
    .nm-cta-outer {
        max-width: 800px;
        margin: 0 auto 52px;
        padding: 0 28px;
        text-align: center;
    }

    /* Override Streamlit's primary button inside CTA zone */
    .nm-cta-zone div.stButton > button {
        width: 100% !important;
        padding: 22px 48px !important;
        font-size: 17px !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em !important;
        border-radius: var(--r-xl) !important;
        background: linear-gradient(135deg,
            var(--green-500)  0%,
            var(--teal-500)   50%,
            #0891B2           100%) !important;
        color: white !important;
        box-shadow: var(--shadow-cta) !important;
        border: none !important;
        transition: all var(--t-mid) var(--ease-spring) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    .nm-cta-zone div.stButton > button::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(255,255,255,0.12), transparent);
        pointer-events: none;
    }
    .nm-cta-zone div.stButton > button:hover {
        transform: translateY(-3px) scale(1.01) !important;
        box-shadow: 0 20px 60px rgba(16,185,129,0.45),
                    0 8px 24px rgba(0,0,0,0.4) !important;
    }
    .nm-cta-zone div.stButton > button:active {
        transform: translateY(0) scale(0.99) !important;
    }

    .nm-cta-trust {
        margin-top: 14px;
        font-size: 13px;
        color: var(--text-muted);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
    }
    .nm-cta-trust-item {
        display: flex;
        align-items: center;
        gap: 5px;
    }
    .nm-cta-trust-item::before {
        content: '✓';
        color: var(--green-500);
        font-weight: 800;
        font-size: 13px;
    }

    /* ═══════════════════════════════════════════════════
       INPUT AREA
    ═══════════════════════════════════════════════════ */
    .nm-input-zone {
        background: rgba(6, 10, 18, 0.88);
        border-top: 1px solid var(--border-glass);
        padding: 18px 32px 22px;
        backdrop-filter: blur(24px) saturate(1.4);
    }
    .nm-input-inner {
        max-width: 800px;
        margin: 0 auto;
    }

    /* ═══════════════════════════════════════════════════
       TOAST
    ═══════════════════════════════════════════════════ */
    .nm-toast {
        max-width: 800px;
        margin: 0 auto 20px;
        padding: 0 28px;
    }
    .nm-toast-inner {
        background: rgba(16,185,129,0.08);
        border: 1px solid rgba(52,211,153,0.25);
        border-radius: var(--r-md);
        padding: 14px 20px;
        font-size: 14px;
        color: var(--green-300);
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 10px;
        backdrop-filter: blur(8px);
    }

    /* ═══════════════════════════════════════════════════
       CONTROL BAR LANG LABEL
    ═══════════════════════════════════════════════════ */
    .nm-lang-label {
        font-size: 11px;
        font-weight: 700;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.1em;
        white-space: nowrap;
    }

    /* ═══════════════════════════════════════════════════
       RESPONSIVE
    ═══════════════════════════════════════════════════ */
    @media (max-width: 640px) {
        .nm-compare-grid  { grid-template-columns: 1fr; }
        .nm-metrics-row   { flex-direction: column; }
        .nm-result-card   { padding: 24px 22px; }
        .nm-hero-amount   { font-size: 42px; }
        .nm-steps-row     { display: none; }
    }

    /* ═══════════════════════════════════════════════════
       BOOKING CONFIRMATION PANEL
    ═══════════════════════════════════════════════════ */
    .nm-booking-outer {
        max-width: 800px;
        margin: 0 auto 28px;
        padding: 0 28px;
    }
    .nm-booking-card {
        background: var(--bg-glass-card);
        border: 1px solid var(--border-green);
        border-radius: var(--r-xl);
        padding: 32px 36px;
        backdrop-filter: blur(20px);
        box-shadow: var(--shadow-green), var(--shadow-card);
        position: relative;
        overflow: hidden;
    }
    .nm-booking-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, var(--green-500), var(--teal-400));
        border-radius: var(--r-xl) var(--r-xl) 0 0;
    }
    .nm-booking-title {
        font-size: 17px;
        font-weight: 800;
        color: var(--text-primary);
        letter-spacing: -0.02em;
        margin-bottom: 20px;
    }
    .nm-booking-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 11px 0;
        border-top: 1px solid var(--border);
        font-size: 14px;
        color: var(--text-secondary);
    }
    .nm-booking-row strong {
        color: var(--text-primary);
        font-family: var(--font-mono);
        font-weight: 700;
    }
    .nm-booking-row.highlight { color: var(--green-300); }
    .nm-booking-row.highlight strong { color: var(--green-300); font-size: 15px; }
    .nm-booking-note {
        margin-top: 18px;
        font-size: 12px;
        color: var(--amber-400);
        padding: 9px 14px;
        background: rgba(245, 158, 11, 0.06);
        border: 1px solid rgba(245, 158, 11, 0.18);
        border-radius: var(--r-sm);
        line-height: 1.6;
    }

    /* ═══════════════════════════════════════════════════
       WHY THIS BANK PANEL
    ═══════════════════════════════════════════════════ */
    .nm-why-outer {
        max-width: 800px;
        margin: 0 auto 28px;
        padding: 0 28px;
    }
    .nm-why-card {
        background: rgba(13, 20, 38, 0.65);
        border: 1px solid var(--border-purple);
        border-radius: var(--r-xl);
        padding: 24px 28px;
        backdrop-filter: blur(16px);
        position: relative;
        overflow: hidden;
    }
    .nm-why-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, var(--purple-500), var(--blue-500));
        border-radius: var(--r-xl) var(--r-xl) 0 0;
    }
    .nm-why-title {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        color: var(--purple-400);
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .nm-why-item {
        display: flex;
        gap: 12px;
        align-items: flex-start;
        padding: 10px 0;
        border-top: 1px solid var(--border);
        font-size: 13.5px;
        color: var(--text-secondary);
        line-height: 1.6;
    }
    .nm-why-icon {
        font-size: 16px;
        flex-shrink: 0;
        margin-top: 2px;
    }

    /* ═══════════════════════════════════════════════════
       TRUST INDICATORS
    ═══════════════════════════════════════════════════ */
    .nm-trust-row {
        max-width: 800px;
        margin: 0 auto 8px;
        padding: 0 28px;
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
    }
    .nm-trust-item {
        display: flex;
        align-items: center;
        gap: 7px;
        font-size: 12px;
        font-weight: 600;
        color: var(--text-muted);
        letter-spacing: 0.02em;
    }
    .nm-trust-icon {
        font-size: 14px;
    }
    .nm-trust-item.green { color: var(--green-500); }
    .nm-trust-item.blue  { color: var(--blue-400);  }
    .nm-trust-item.amber { color: var(--amber-400); }

    /* ═══════════════════════════════════════════════════
       EDIT INPUT BUTTONS
    ═══════════════════════════════════════════════════ */
    .nm-edit-bar {
        max-width: 800px;
        margin: 0 auto 24px;
        padding: 0 28px;
        display: flex;
        gap: 10px;
    }
    .nm-edit-btn-wrap {
        flex: 1;
    }

    /* ═══════════════════════════════════════════════════
       VOICE MIC BUTTON
    ═══════════════════════════════════════════════════ */
    .nm-voice-processing {
        max-width: 800px;
        margin: 0 auto 8px;
        padding: 0 28px;
        font-size: 13px;
        color: var(--blue-300);
        display: flex;
        align-items: center;
        gap: 8px;
        animation: voice-pulse 1.4s ease-in-out infinite;
    }
    @keyframes voice-pulse {
        0%, 100% { opacity: 1; }
        50%       { opacity: 0.4; }
    }
    </style>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────────────────────

def render_header(current_step: int = 1):
    """
    current_step: 1 = chat, 2 = results shown, 3 = booking
    """
    steps = [
        (1, "Enter Amount"),
        (2, "View Returns"),
        (3, "Book FD"),
    ]
    steps_html = ""
    for i, (num, label) in enumerate(steps):
        if current_step > num:
            cls = "done"
        elif current_step == num:
            cls = "active"
        else:
            cls = ""

        steps_html += f"""
        <div class="nm-step {cls}">
            <div class="nm-step-num">{("✓" if current_step > num else num)}</div>
            {label}
        </div>"""
        if i < len(steps) - 1:
            steps_html += '<div class="nm-step-line"></div>'

    st.markdown(f"""
    <div class="nm-header">
        <div class="nm-header-badge">
            <span class="live-dot"></span>
            AI-Powered Investment Assistant
        </div>
        <h1 class="nm-title">💰 Nivesh Mitra AI</h1>
        <div class="nm-tagline">
        <span>FD returns in seconds — in your own language.</span><br>
        <span>Trusted by lakhs of everyday investors across India.</span>
        </div>
        <div class="nm-steps-row">{steps_html}</div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  CONTROL BAR
# ─────────────────────────────────────────────────────────────

def render_control_bar():
    """Returns (selected_language, mic_clicked)."""
    st.markdown('<div class="nm-control-bar">', unsafe_allow_html=True)

    col_label, col_lang, col_spacer, col_mic = st.columns([1.2, 3, 9, 1])

    with col_label:
        st.markdown(
            '<div class="nm-lang-label" style="padding-top:10px">🌐 Lang</div>',
            unsafe_allow_html=True,
        )
    with col_lang:
        lang = st.selectbox(
            label="language",
            options=["English", "हिंदी", "தமிழ்", "తెలుగు", "বাংলা", "मराठी", "ਪੰਜਾਬੀ"],
            label_visibility="collapsed",
            key="language_select",
        )
    with col_mic:
        mic = st.button("🎤", key="mic_btn", help="Voice Input",
                        use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
    return lang, mic


# ─────────────────────────────────────────────────────────────
#  CHAT MESSAGES
# ─────────────────────────────────────────────────────────────

def render_chat_message(role: str, content: str, timestamp: str = ""):
    """role: 'user' | 'bot'"""
    avatar = "🤖" if role == "bot" else "👤"
    ts_html = f'<div class="nm-timestamp">{timestamp}</div>' if timestamp else ""
    # Escape any HTML tags so they never render inside the bubble.
    # Then convert newlines to <br> so line-breaks still display.
    safe_content = html.escape(content).replace("\n", "<br>")

    if role == "user":
        st.markdown(f"""
        <div class="nm-chat-row user">
            <div class="nm-bubble-wrap" style="align-items:flex-end">
                <div class="nm-bubble user">{safe_content}</div>
                {ts_html}
            </div>
            <div class="nm-avatar user">{avatar}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="nm-chat-row bot">
            <div class="nm-avatar bot">{avatar}</div>
            <div class="nm-bubble-wrap" style="align-items:flex-start">
                <div class="nm-bubble bot">{safe_content}</div>
                {ts_html}
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_typing_indicator():
    st.markdown("""
    <div class="nm-typing">
        <div class="nm-avatar bot">🤖</div>
        <div class="nm-typing-dots">
            <span></span><span></span><span></span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_empty_state():
    st.markdown("""
    <div class="nm-empty">
        <span class="nm-empty-icon">💬</span>
        <div class="nm-empty-title">Namaste! How can I help?</div>
        <div class="nm-empty-sub">
            Tell me how much you want to invest and for how long —
            I'll find the best Fixed Deposit for you, in plain language.
        </div>
        <div class="nm-chips">
            <span class="nm-chip">📊 Best FD rates today</span>
            <span class="nm-chip">🏦 SBI vs HDFC FD</span>
            <span class="nm-chip">💡 FD for ₹1 lakh, 1 year</span>
            <span class="nm-chip">🔒 Senior citizen rates</span>
            <span class="nm-chip">📅 FD for 5 years</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  SECTION LABEL
# ─────────────────────────────────────────────────────────────

def render_section_label(text: str):
    st.markdown(f"""
    <div class="nm-section">
        <div class="nm-section-label">{text}</div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  HERO RESULT CARD
# ─────────────────────────────────────────────────────────────

def render_fd_result_card(
    principal: float,
    interest_earned: float,
    total_amount: float,
    tenure: str = "",
    rate: float = 0.0,
):
    rate_str = f"{rate:.2f}%" if rate else "—"
    gain_pct = (interest_earned / principal * 100) if principal else 0
    # NOTE: No blank lines inside the HTML — Streamlit's markdown parser exits
    # HTML mode at the first blank line, causing everything after to render as
    # escaped text. Keep this as a flat, newline-free concatenated string.
    st.markdown(
        '<div class="nm-result-outer">'
        '<div class="nm-result-card">'
        '<div class="nm-result-eyebrow">Your FD Maturity Summary</div>'
        f'<div class="nm-result-headline">Based on {tenure} at {rate_str} p.a. interest</div>'
        '<div class="nm-hero-amount-label">🏁 &nbsp;Total Maturity Amount</div>'
        f'<div class="nm-hero-amount">₹{total_amount:,.0f}</div>'
        f'<div class="nm-hero-sub">Your money grew by {gain_pct:.1f}% in {tenure}</div>'
        '<div class="nm-metrics-row">'
        '<div class="nm-metric-pill">'
        '<span class="nm-metric-icon">💰</span>'
        '<div class="nm-metric-lbl">Principal</div>'
        f'<div class="nm-metric-val blue">₹{principal:,.0f}</div>'
        '<div class="nm-metric-note">Amount invested</div>'
        '</div>'
        '<div class="nm-metric-pill">'
        '<span class="nm-metric-icon">📈</span>'
        '<div class="nm-metric-lbl">Interest Earned</div>'
        f'<div class="nm-metric-val amber">₹{interest_earned:,.0f}</div>'
        f'<div class="nm-metric-note">@ {rate_str} p.a.</div>'
        '</div>'
        '<div class="nm-metric-pill">'
        '<span class="nm-metric-icon">🗓️</span>'
        '<div class="nm-metric-lbl">Tenure</div>'
        f'<div class="nm-metric-val green">{tenure}</div>'
        '<div class="nm-metric-note">Lock-in period</div>'
        '</div>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ─────────────────────────────────────────────────────────────
#  COMPARISON CARDS
# ─────────────────────────────────────────────────────────────

def render_fd_comparison(bank_a: dict, bank_b: dict):

    def _card(bank):
        is_winner = bank.get("highlight", False)
        card_cls  = "winner" if is_winner else "loser"
        rate_cls  = "green" if is_winner else "blue"

        badge_html = (
            '<div class="nm-best-badge">🏆 Best Option</div>'
            if is_winner else ""
        )

        # One-liner per stat — no blank lines or newlines that would cause the
        # markdown parser to exit HTML mode and escape the rest as plain text.
        stats_html = "".join(
            f'<div class="nm-compare-stat">'
            f'<span>{lbl}</span>'
            f'<span class="nm-compare-stat-val">{val}</span>'
            f'</div>'
            for lbl, val in bank.get("stats", {}).items()
        )

        earn_html = (
            f'<div class="nm-earn-more">💡 {bank["earn_more"]}</div>'
            if is_winner and bank.get("earn_more") else ""
        )

        # Build card as a flat string — no blank lines, no surrounding whitespace.
        return (
            f'<div class="nm-compare-card {card_cls}">'
            + badge_html
            + f'<div class="nm-bank-name">{bank["name"]}</div>'
            + '<div class="nm-bank-sub">Fixed Deposit</div>'
            + f'<div class="nm-compare-rate {rate_cls}">{bank["rate"]}%</div>'
            + '<div class="nm-compare-rate-lbl">Annual Interest Rate</div>'
            + stats_html
            + earn_html
            + '</div>'
        )

    html = (
        '<div class="nm-compare-outer">'
        '<div class="nm-compare-grid">'
        + _card(bank_a)
        + _card(bank_b)
        + '</div>'
        '</div>'
    )

    st.markdown(html, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  CTA BUTTON
# ─────────────────────────────────────────────────────────────

def render_cta_button(label: str = "🚀  Proceed to Booking", sub: str = ""):
    st.markdown('<div class="nm-cta-outer"><div class="nm-cta-zone">', unsafe_allow_html=True)
    clicked = st.button(label, key="cta_proceed", use_container_width=True, type="primary")
    st.markdown(f"""
        <div class="nm-cta-trust">
            <span class="nm-cta-trust-item">100% Paperless</span>
            <span class="nm-cta-trust-item">Bank-Grade Security</span>
            <span class="nm-cta-trust-item">Under 3 Minutes</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)
    return clicked


# ─────────────────────────────────────────────────────────────
#  TOAST / ALERT
# ─────────────────────────────────────────────────────────────

def render_toast(message: str):
    st.markdown(f"""
    <div class="nm-toast">
        <div class="nm-toast-inner">✅ &nbsp;{message}</div>
    </div>
    """, unsafe_allow_html=True)