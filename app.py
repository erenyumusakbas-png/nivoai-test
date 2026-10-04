import streamlit as st

st.set_page_config(
    page_title="NIVO — Cognitive Balance Operating System",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom High-End Cyber Blue / Deep Obsidian Dark Design System
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #06090e;
    color: #e2e8f0;
}

.stApp {
    background: radial-gradient(circle at 50% -20%, #0d2238 0%, #070e17 40%, #04070c 100%);
}

#MainMenu, header, footer {visibility: hidden;}
.block-container {
    padding-top: 1.8rem;
    padding-bottom: 3rem;
    max-width: 1140px;
}

/* Glassmorphism Card Architecture */
.nivo-card {
    background: linear-gradient(135deg, rgba(13, 27, 44, 0.65) 0%, rgba(9, 17, 28, 0.85) 100%);
    border: 1px solid rgba(56, 189, 248, 0.18);
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 12px 32px -12px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(14px);
    margin-bottom: 18px;
    transition: border-color 0.25s ease, box-shadow 0.25s ease;
}

.nivo-card:hover {
    border-color: rgba(56, 189, 248, 0.38);
    box-shadow: 0 14px 36px -10px rgba(14, 165, 233, 0.18);
}

/* Premium Navigation Header */
.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 26px;
    background: rgba(10, 18, 30, 0.75);
    border: 1px solid rgba(56, 189, 248, 0.22);
    border-radius: 18px;
    backdrop-filter: blur(20px);
    margin-bottom: 28px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
}

.brand-wrapper {
    display: flex;
    align-items: center;
    gap: 14px;
}

.brand-name {
    font-size: 23px;
    font-weight: 800;
    letter-spacing: 0.2em;
    background: linear-gradient(135deg, #ffffff 20%, #7dd3fc 70%, #0284c7 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.status-badge {
    background: rgba(14, 165, 233, 0.12);
    color: #38bdf8;
    border: 1px solid rgba(56, 189, 248, 0.32);
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 7px;
}

.status-pulse {
    width: 7px;
    height: 7px;
    background: #0ea5e9;
    border-radius: 50%;
    box-shadow: 0 0 10px #38bdf8;
}

/* Forms & Interactive Elements */
.stTextArea textarea {
    background-color: rgba(9, 18, 30, 0.85) !important;
    color: #f8fafc !important;
    border: 1px solid rgba(56, 189, 248, 0.24) !important;
    border-radius: 12px !important;
    font-size: 14px !important;
}

.stTextArea textarea:focus {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2) !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: rgba(9, 18, 30, 0.85) !important;
    border: 1px solid rgba(56, 189, 248, 0.24) !important;
    border-radius: 12px !important;
    color: #f8fafc !important;
}

div.stButton > button {
    background: linear-gradient(135deg, #0369a1 0%, #0284c7 50%, #0ea5e9 100%) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    letter-spacing: 0.05em !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 12px !important;
    padding: 0.72rem 1.6rem !important;
    box-shadow: 0 4px 22px rgba(14, 165, 233, 0.35) !important;
    transition: all 0.25s ease !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 28px rgba(56, 189, 248, 0.55) !important;
}

.tag-badge {
    background: rgba(14, 165, 233, 0.15);
    color: #7dd3fc;
    border: 1px solid rgba(56, 189, 248, 0.28);
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 11px;
    font-weight: 600;
}
</style>""", unsafe_allow_html=True)

# Custom SVG Brand Logo for NIVO (Geometric Water-Level Balance Balance Concept)
LOGO_SVG = """<svg width="42" height="42" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="nivo_blue" x1="0" y1="0" x2="48" y2="48" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#bae6fd" />
      <stop offset="45%" stop-color="#0ea5e9" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
    <linearGradient id="glow_grad" x1="0" y1="0" x2="48" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0.3"/>
    </linearGradient>
  </defs>
  <rect width="48" height="48" rx="14" fill="#081423"/>
  <rect x="0.75" y="0.75" width="46.5" height="46.5" rx="13.25" stroke="url(#nivo_blue)" stroke-opacity="0.45"/>
  <path d="M14 34V14L24 28L34 14V34" stroke="url(#nivo_blue)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="12" y1="38" x2="36" y2="38" stroke="url(#glow_grad)" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="24" cy="38" r="2.2" fill="#38bdf8"/>
</svg>"""

navbar_html = f"""<div class="nav-container">
<div class="brand-wrapper">
{LOGO_SVG}
<div>
<div class="brand-name">NIVO</div>
<div style="font-size: 10px; color: #7dd3fc; letter-spacing: 0.12em; text-transform: uppercase;">Cognitive Balance Operating System</div>
</div>
</div>
<div class="status-badge"><span class="status-pulse"></span> Privacy Core Online</div>
</div>"""

st.markdown(navbar_html, unsafe_allow_html=True)

# State initialization
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"title": "Eczane ve İlaç Temini", "due": "Yarın 10:00", "owner": "Buse", "tag": "Lojistik"},
        {"title": "Mutfak Derin Temizlik", "due": "Bugün 20:00", "owner": "Hakan", "tag": "Ev Düzeni"},
        {"title": "Aylık Kira & Fatura Masrafları", "due": "15 Ekim", "owner": "Hakan", "tag": "Finans"}
    ]

col_left, col_right = st.columns([1.18, 1], gap="large")

with col_left:
    st.markdown("""<div class="nivo-card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
<div style="font-weight:700; font-size:16px; color:#f8fafc;">WhatsApp & Doğal Dil Akışı</div>
<span style="font-size:11px; color:#38bdf8; font-family:monospace;">E2EE Neural Hook</span>
</div>""", unsafe_allow_html=True)

    input_text = st.text_area(
        label="Mesaj İçeriği",
        label_visibility="collapsed",
        placeholder="WhatsApp'tan bir mesaj girin: 'Buse yarın marketten kahve alabilir misin, ben de akşam evi toparlarım.'",
        height=95
    )

    c_in1, c_in2 = st.columns([1, 1])
    with c_in1:
        actor = st.selectbox("Mesajı İleten:", ["Hakan", "Buse"], label_visibility="collapsed")
    with c_in2:
        sync_btn = st.button("Senkronize Et ⚡", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if sync_btn and input_text.strip():
        raw_lower = input_text.lower()
        detected_task = "Rutin Koordinasyon"
        time_window = "En Kısa Sürede"
        category = "Genel"

        if any(w in raw_lower for w in ["veteriner", "kedi", "mama", "köpek"]):
            detected_task = "Kedi & Veteriner İhtiyaçları"
            category = "Evcil Hayvan"
        elif any(w in raw_lower for w in ["eczane", "ilaç", "sağlık", "doktor"]):
            detected_task = "Eczane & Sağlık Temini"
            category = "Sağlık"
        elif any(w in raw_lower for w in ["market", "kahve", "ekmek", "süt", "sipariş"]):
            detected_task = "Haftalık Market Tedariği"
            category = "Lojistik"
        elif any(w in raw_lower for w in ["fatura", "kira", "ödeme", "kart"]):
            detected_task = "Bütçe ve Fatura Denkleştirme"
            category = "Finans"
        elif any(w in raw_lower for w in ["temizlik", "mutfak", "çöp", "bulaşık", "süpür"]):
            detected_task = "Ev Organizasyonu & Hijyen"
            category = "Ev Düzeni"
        else:
            detected_task = input_text[:38].strip() + "..."

        if "yarın" in raw_lower:
            time_window = "Yarın"
        elif "akşam" in raw_lower:
            time_window = "Bu Akşam"
        elif "hafta sonu" in raw_lower:
            time_window = "Hafta Sonu"

        st.session_state.tasks.insert(0, {
            "title": detected_task,
            "due": time_window,
            "owner": actor,
            "tag": category
        })
        st.rerun()

    st.markdown("### 📋 Aktif Zihinsel Envanter")
    for t in st.session_state.tasks:
        card_markup = f"""<div class="nivo-card" style="padding:16px 20px; margin-bottom:12px;">
<div style="display:flex; justify-content:space-between; align-items:flex-start;">
<div>
<div style="font-weight:600; font-size:15px; color:#f8fafc; margin-bottom:6px;">{t['title']}</div>
<div style="font-size:12px; color:#94a3b8;">⏱️ {t['due']} &nbsp;•&nbsp; 👤 <b>{t['owner']}</b></div>
</div>
<span class="tag-badge">{t['tag']}</span>
</div>
</div>"""
        st.markdown(card_markup, unsafe_allow_html=True)

with col_right:
    st.markdown("### ⚖️ Yük Denge Analitiği")

    total_tasks = len(st.session_state.tasks)
    hakan_tasks = sum(1 for t in st.session_state.tasks if t["owner"] == "Hakan")
    buse_tasks = sum(1 for t in st.session_state.tasks if t["owner"] == "Buse")

    hakan_ratio = round((hakan_tasks / total_tasks * 100)) if total_tasks > 0 else 50
    buse_ratio = 100 - hakan_ratio if total_tasks > 0 else 50

    st.markdown("""<div class="nivo-card">
<div style="font-size:12px; font-weight:700; color:#38bdf8; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:16px;">
Bilişsel Efor İndeksi (Nivo Skoru)
</div>""", unsafe_allow_html=True)

    m1, m2 = st.columns(2)
    with m1:
        st.metric(label="Hakan Sorumluluğu", value=f"%{hakan_ratio}", delta=f"{hakan_tasks} aktif görev")
    with m2:
        st.metric(label="Buse Sorumluluğu", value=f"%{buse_ratio}", delta=f"{buse_tasks} aktif görev")

    st.progress(hakan_ratio / 100)
    st.markdown("</div>", unsafe_allow_html=True)

    status_text = (
        "Sistem şu anda dengeli bir bilişsel iş yükü dağılımı öngörüyor. İki tarafın sorumlulukları senkronize ilerliyor."
        if abs(hakan_ratio - buse_ratio) <= 15
        else "Zihinsel yük dağılımında sapma tespit edildi. Yeni görevlerin dengelenmesi önerilir."
    )

    info_card = f"""<div class="nivo-card">
<div style="font-size:13px; font-weight:700; color:#f8fafc; margin-bottom:8px;">Haftalık Görünmez Yük Dengesi</div>
<div style="font-size:13px; color:#94a3b8; line-height:1.6;">{status_text}</div>
</div>"""
    st.markdown(info_card, unsafe_allow_html=True)
    
    privacy_card = """<div class="nivo-card" style="border-color: rgba(56, 189, 248, 0.15);">
<div style="font-size:12px; font-weight:700; color:#7dd3fc; margin-bottom:6px;">🛡️ Sıfır Konuşma Saklama Protokolü</div>
<div style="font-size:12px; color:#64748b; line-height:1.5;">WhatsApp üzerinden iletilen mesajlar anlık JSON dönüşümünün ardından silinir; veri tabanında ham sohbet içeriği saklanmaz.</div>
</div>"""
    st.markdown(privacy_card, unsafe_allow_html=True)
