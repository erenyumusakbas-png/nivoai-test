import streamlit as st

st.set_page_config(
    page_title="NIVO — Cognitive Balance OS",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Ultra-Refined Anthracite Titanium & Mobile Responsive System
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg-base: #090b0e;
    --card-surface: #12151d;
    --card-surface-hover: #171c26;
    --border-subtle: rgba(255, 255, 255, 0.08);
    --border-highlight: rgba(148, 163, 184, 0.28);
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --text-tertiary: #64748b;
    --accent-titanium: #cbd5e1;
    --accent-cyan: #38bdf8;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: var(--bg-base);
    color: var(--text-primary);
    -webkit-font-smoothing: antialiased;
}

.stApp {
    background: radial-gradient(circle at 50% -12%, #1a202c 0%, #0b0e13 55%, #06070a 100%);
}

#MainMenu, header, footer {visibility: hidden; display: none;}
.block-container {
    padding-top: 1.2rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 1080px !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}

/* Nivo Cards */
.nivo-card {
    background: var(--card-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 14px;
    padding: 18px 20px;
    box-shadow: 0 4px 22px -4px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.04);
    margin-bottom: 12px;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.nivo-card:hover {
    border-color: var(--border-highlight);
    background: var(--card-surface-hover);
}

/* Navigation Shell */
.nav-shell {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 18px;
    background: rgba(15, 18, 25, 0.85);
    border: 1px solid var(--border-subtle);
    border-radius: 16px;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    margin-bottom: 22px;
}

.brand-combo {
    display: flex;
    align-items: center;
    gap: 14px;
}

.brand-text-nivo {
    font-size: 21px;
    font-weight: 800;
    letter-spacing: 0.18em;
    color: #ffffff;
    line-height: 1.1;
}

.brand-subline {
    font-size: 9.5px;
    color: var(--text-tertiary);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    font-weight: 600;
}

.badge-pill {
    background: rgba(255, 255, 255, 0.04);
    color: var(--accent-titanium);
    border: 1px solid var(--border-subtle);
    padding: 5px 12px;
    border-radius: 9999px;
    font-size: 10.5px;
    font-weight: 600;
    letter-spacing: 0.04em;
    display: flex;
    align-items: center;
    gap: 6px;
}

.dot-indicator {
    width: 6px;
    height: 6px;
    background: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 8px rgba(16, 185, 129, 0.7);
}

/* Input Fields */
.stTextArea textarea {
    background-color: #0e1117 !important;
    color: #f8fafc !important;
    border: 1px solid var(--border-subtle) !important;
    border-radius: 12px !important;
    font-size: 13.5px !important;
    padding: 12px !important;
}

.stTextArea textarea:focus {
    border-color: rgba(255, 255, 255, 0.3) !important;
    box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.15) !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: #0e1117 !important;
    border: 1px solid var(--border-subtle) !important;
    border-radius: 12px !important;
    color: #f8fafc !important;
    min-height: 42px !important;
}

div.stButton > button {
    background: linear-gradient(180deg, #2b3340 0%, #1c222c 100%) !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    font-size: 13.5px !important;
    border: 1px solid rgba(255, 255, 255, 0.14) !important;
    border-radius: 12px !important;
    padding: 0.65rem 1.2rem !important;
    min-height: 42px !important;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.4) !important;
}

div.stButton > button:hover {
    background: linear-gradient(180deg, #374152 0%, #252e3c 100%) !important;
    border-color: rgba(255, 255, 255, 0.28) !important;
}

/* Metric Display System */
.metric-tile {
    background: #0d1016;
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 14px 16px;
}

.metric-label {
    font-size: 11px;
    font-weight: 600;
    color: var(--text-tertiary);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 4px;
}

.metric-value-lg {
    font-size: 22px;
    font-weight: 800;
    color: #ffffff;
    display: flex;
    align-items: baseline;
    gap: 6px;
}

.badge-tag {
    background: rgba(255, 255, 255, 0.05);
    color: #cbd5e1;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 6px;
    padding: 3px 8px;
    font-size: 10px;
    font-weight: 600;
}

.effort-indicator {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    padding: 2px 7px;
    border-radius: 4px;
    background: rgba(56, 189, 248, 0.1);
    color: #7dd3fc;
    border: 1px solid rgba(56, 189, 248, 0.2);
}

.balance-track {
    width: 100%;
    height: 8px;
    background: #171c26;
    border-radius: 9999px;
    overflow: hidden;
    display: flex;
    margin-top: 14px;
}

.balance-fill-left {
    background: linear-gradient(90deg, #475569, #cbd5e1);
    height: 100%;
    transition: width 0.3s ease;
}

.balance-fill-right {
    background: #1e293b;
    height: 100%;
    transition: width 0.3s ease;
}
</style>""", unsafe_allow_html=True)

# Custom High-End NIVO Precision Level Logo (SVG)
NIVO_LOGO_SVG = """<svg width="42" height="42" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="nivoBg" cx="50%" cy="20%" r="90%">
      <stop offset="0%" stop-color="#1e2430"/>
      <stop offset="100%" stop-color="#0e1218"/>
    </radialGradient>
    <linearGradient id="nivoBorder" x1="0" y1="0" x2="48" y2="48" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#475569" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#334155" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#1e293b" stop-opacity="0.8"/>
    </linearGradient>
    <linearGradient id="nivoGleam" x1="12" y1="12" x2="36" y2="36" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
    <linearGradient id="levelBeam" x1="12" y1="37" x2="36" y2="37" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.2"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.2"/>
    </linearGradient>
  </defs>
  <rect width="48" height="48" rx="13" fill="url(#nivoBg)"/>
  <rect x="0.75" y="0.75" width="46.5" height="46.5" rx="12.25" stroke="url(#nivoBorder)" stroke-width="1.5"/>
  <path d="M15 32V16L24 27.5L33 16V32" stroke="url(#nivoGleam)" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="13" y1="37" x2="35" y2="37" stroke="url(#levelBeam)" stroke-width="2" stroke-linecap="round"/>
  <circle cx="24" cy="37" r="2.2" fill="#38bdf8"/>
  <circle cx="24" cy="37" r="0.9" fill="#ffffff"/>
</svg>"""

navbar_html = f"""<div class="nav-shell">
<div class="brand-combo">
{NIVO_LOGO_SVG}
<div>
<div class="brand-text-nivo">NIVO</div>
<div class="brand-subline">Cognitive Balance Operating System</div>
</div>
</div>
<div class="badge-pill"><span class="dot-indicator"></span> E2EE Active</div>
</div>"""

st.markdown(navbar_html, unsafe_allow_html=True)

# Initial Extended Task State
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"id": 1, "title": "Kedinin Aşı Takvimi & Veteriner Randevusu", "due": "Salı 14:00", "owner": "Buse", "tag": "Evcil Hayvan", "weight": 3},
        {"id": 2, "title": "Yıllık Ev & Araç Sigorta Karşılaştırması", "due": "18 Ekim", "owner": "Hakan", "tag": "Finans", "weight": 3},
        {"id": 3, "title": "Haftalık Sağlıklı Yemek & Market Planı", "due": "Bu Akşam", "owner": "Buse", "tag": "Lojistik", "weight": 2},
        {"id": 4, "title": "Kombi Yıllık Bakımı ve Servis Araması", "due": "Cuma 11:00", "owner": "Hakan", "tag": "Ev Düzeni", "weight": 2},
        {"id": 5, "title": "Mutfak Derin Hijyen ve Düzenleme", "due": "Hafta Sonu", "owner": "Hakan", "tag": "Ev Düzeni", "weight": 1},
    ]

col_left, col_right = st.columns([1.12, 1], gap="medium")

with col_left:
    st.markdown("""<div class="nivo-card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
<div style="font-weight:700; font-size:14px; color:#f1f5f9;">WhatsApp Doğal Dil Asistanı</div>
<span style="font-size:10.5px; color:#94a3b8; font-family:'JetBrains Mono', monospace;">Zero-Retention Hook</span>
</div>""", unsafe_allow_html=True)

    input_text = st.text_area(
        label="Mesaj İçeriği",
        label_visibility="collapsed",
        placeholder="WhatsApp mesajı yapıştırın: 'Buse yarın kedinin mamasını sipariş edebilir misin, ben de kombi servisini ararım.'",
        height=85
    )

    c_in1, c_in2 = st.columns([1, 1])
    with c_in1:
        actor = st.selectbox("Mesaj Sahibi:", ["Hakan", "Buse"], label_visibility="collapsed")
    with c_in2:
        sync_btn = st.button("Senkronize Et ⚡", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Dynamic Parsing Engine
    if sync_btn and input_text.strip():
        raw_lower = input_text.lower()
        detected_task = "Rutin Koordinasyon"
        time_window = "Yakında"
        category = "Genel"
        task_weight = 1

        if any(w in raw_lower for w in ["veteriner", "kedi", "mama", "köpek", "aşı"]):
            detected_task = "Evcil Hayvan Sağlık & Tedarik"
            category = "Evcil Hayvan"
            task_weight = 3
        elif any(w in raw_lower for w in ["eczane", "ilaç", "doktor", "hastane", "sağlık"]):
            detected_task = "Sağlık & Eczane İhtiyaçları"
            category = "Sağlık"
            task_weight = 2
        elif any(w in raw_lower for w in ["fatura", "kira", "sigorta", "bütçe", "kredi", "vergi"]):
            detected_task = "Mali Yönetim & Fatura Denkleştirme"
            category = "Finans"
            task_weight = 3
        elif any(w in raw_lower for w in ["market", "kahve", "sipariş", "yemek", "manav"]):
            detected_task = "Mutfak & Market Lojistiği"
            category = "Lojistik"
            task_weight = 2
        elif any(w in raw_lower for w in ["temizlik", "kombi", "servis", "tamir", "çöp", "bulaşık"]):
            detected_task = "Ev Bakımı & Düzenleme"
            category = "Ev Düzeni"
            task_weight = 2
        else:
            detected_task = input_text[:38].strip() + "..."

        if "yarın" in raw_lower:
            time_window = "Yarın"
        elif "akşam" in raw_lower:
            time_window = "Bu Akşam"
        elif "hafta sonu" in raw_lower:
            time_window = "Hafta Sonu"

        new_id = max([t["id"] for t in st.session_state.tasks], default=0) + 1
        st.session_state.tasks.insert(0, {
            "id": new_id,
            "title": detected_task,
            "due": time_window,
            "owner": actor,
            "tag": category,
            "weight": task_weight
        })
        st.rerun()

    # Active Inventory & Interactive Completion
    st.markdown("<div style='font-size:14px; font-weight:700; color:#cbd5e1; margin: 16px 0 10px 4px;'>📋 Aktif Zihinsel Envanter</div>", unsafe_allow_html=True)
    
    if st.session_state.tasks:
        for t in list(st.session_state.tasks):
            t_col1, t_col2 = st.columns([5.2, 1])
            with t_col1:
                weight_stars = "⚡" * t.get("weight", 1)
                task_html = f"""<div class="nivo-card" style="padding:14px 16px; margin-bottom:6px;">
<div style="display:flex; justify-content:space-between; align-items:flex-start; gap:8px;">
<div>
<div style="font-weight:600; font-size:13.5px; color:#f8fafc; margin-bottom:4px;">{t['title']}</div>
<div style="font-size:11.5px; color:#94a3b8;">⏱️ {t['due']} &nbsp;•&nbsp; 👤 <b>{t['owner']}</b></div>
</div>
<div style="display:flex; gap:6px; align-items:center;">
<span class="effort-indicator" title="Bilişsel Efor Derecesi">{weight_stars}</span>
<span class="badge-tag">{t['tag']}</span>
</div>
</div>
</div>"""
                st.markdown(task_html, unsafe_allow_html=True)
            with t_col2:
                if st.button("Tamam", key=f"done_{t['id']}", help="Görevi tamamlandı olarak işaretle"):
                    st.session_state.tasks = [task for task in st.session_state.tasks if task["id"] != t["id"]]
                    st.rerun()
    else:
        st.info("Harika! Tüm zihinsel yük tamamlandı, aktif görev yok.")

with col_right:
    st.markdown("<div style='font-size:14px; font-weight:700; color:#cbd5e1; margin: 0 0 10px 4px;'>⚖️ Bilişsel Yük Analitiği</div>", unsafe_allow_html=True)

    # Weighted Load Calculations
    hakan_weight = sum(t.get("weight", 1) for t in st.session_state.tasks if t["owner"] == "Hakan")
    buse_weight = sum(t.get("weight", 1) for t in st.session_state.tasks if t["owner"] == "Buse")
    total_weight = hakan_weight + buse_weight

    hakan_ratio = round((hakan_weight / total_weight * 100)) if total_weight > 0 else 50
    buse_ratio = 100 - hakan_ratio if total_weight > 0 else 50

    card_analytics = f"""<div class="nivo-card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
<div style="font-size:11px; font-weight:700; color:#94a3b8; letter-spacing:0.08em; text-transform:uppercase;">
Bilişsel Efor İndeksi (Nivo Skoru)
</div>
<span style="font-size:10px; color:#64748b; font-family:'JetBrains Mono';">Ağırlıklı Puan</span>
</div>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
<div class="metric-tile">
<div class="metric-label">Hakan Efor Yükü</div>
<div class="metric-value-lg">%{hakan_ratio} <span style="font-size:11.5px; color:#64748b; font-weight:500;">({hakan_weight} pts)</span></div>
</div>
<div class="metric-tile">
<div class="metric-label">Buse Efor Yükü</div>
<div class="metric-value-lg">%{buse_ratio} <span style="font-size:11.5px; color:#64748b; font-weight:500;">({buse_weight} pts)</span></div>
</div>
</div>
<div class="balance-track">
<div class="balance-fill-left" style="width:{hakan_ratio}%;"></div>
<div class="balance-fill-right" style="width:{buse_ratio}%;"></div>
</div>
</div>"""
    st.markdown(card_analytics, unsafe_allow_html=True)

    # Intelligent Balance Engine Recommendation
    if abs(hakan_ratio - buse_ratio) <= 15:
        recommendation = "✅ **Denge Optimize:** Zihinsel efor iki taraf arasında eşit dağılmış durumda. İletişim akışı pürüzsüz."
    elif hakan_ratio > buse_ratio:
        recommendation = "💡 **Denge Önerisi:** Hakan üzerinde finans ve servis takibi kaynaklı yoğun bir bilişsel yük var. Sonraki operasyonel işleri Buse'nin devralması önerilir."
    else:
        recommendation = "💡 **Denge Önerisi:** Buse üzerinde evcil hayvan ve rutin planlama sorumluluğu birikmiş durumda. Sıradaki lojistik görevleri Hakan'ın üstlenmesi dengeyi korur."

    recommendation_card = f"""<div class="nivo-card">
<div style="font-size:12.5px; font-weight:700; color:#f8fafc; margin-bottom:6px;">Akıllı Dengeleme Tavsiyesi</div>
<div style="font-size:12px; color:#cbd5e1; line-height:1.5;">{recommendation}</div>
</div>"""
    st.markdown(recommendation_card, unsafe_allow_html=True)

    # Zero-Retention Privacy Module
    protocol_card = """<div class="nivo-card" style="border-style:dashed;">
<div style="font-size:11.5px; font-weight:700; color:#cbd5e1; margin-bottom:4px;">🛡️ Sıfır Konuşma Saklama Protokolü</div>
<div style="font-size:11px; color:#64748b; line-height:1.45;">WhatsApp üzerinden gelen ham sohbet girdileri işlendikten sonra doğrudan RAM üzerinden imha edilir. Gizlilik gereği sunucuda metin tutulmaz.</div>
</div>"""
    st.markdown(protocol_card, unsafe_allow_html=True)
