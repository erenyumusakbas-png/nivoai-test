import streamlit as st

st.set_page_config(
    page_title="NOVA — Mental Load Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom High-End Crimson / Dark Luxury Design System
st.markdown(
    """<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #08080a;
    color: #e6edf3;
}

.stApp {
    background: radial-gradient(circle at 50% -10%, #2e0811 0%, #0d0d12 45%, #070709 100%);
}

#MainMenu, header, footer {visibility: hidden;}
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1100px;
}

.nova-card {
    background: linear-gradient(135deg, rgba(26, 12, 16, 0.7) 0%, rgba(15, 15, 20, 0.85) 100%);
    border: 1px solid rgba(225, 29, 72, 0.22);
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.7);
    margin-bottom: 20px;
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 28px;
    background: rgba(14, 11, 14, 0.7);
    border: 1px solid rgba(225, 29, 72, 0.25);
    border-radius: 20px;
    margin-bottom: 32px;
}

.brand-wrapper {
    display: flex;
    align-items: center;
    gap: 14px;
}

.brand-name {
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 0.18em;
    background: linear-gradient(135deg, #ffffff 30%, #fda4af 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.status-badge {
    background: rgba(225, 29, 72, 0.12);
    color: #fb7185;
    border: 1px solid rgba(225, 29, 72, 0.3);
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

.stTextArea textarea {
    background-color: rgba(15, 12, 16, 0.8) !important;
    color: #f1f5f9 !important;
    border: 1px solid rgba(225, 29, 72, 0.28) !important;
    border-radius: 12px !important;
}

.stTextArea textarea:focus {
    border-color: #e11d48 !important;
    box-shadow: 0 0 0 2px rgba(225, 29, 72, 0.2) !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: rgba(15, 12, 16, 0.8) !important;
    border: 1px solid rgba(225, 29, 72, 0.28) !important;
    border-radius: 12px !important;
    color: #f1f5f9 !important;
}

div.stButton > button {
    background: linear-gradient(135deg, #9f1239 0%, #e11d48 50%, #be123c 100%) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
    padding: 0.75rem 1.6rem !important;
    box-shadow: 0 4px 20px rgba(225, 29, 72, 0.4) !important;
}

.tag-badge {
    background: rgba(225, 29, 72, 0.14);
    color: #fda4af;
    border: 1px solid rgba(225, 29, 72, 0.25);
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 11px;
    font-weight: 600;
}
</style>""",
    unsafe_allow_html=True,
)

# Navbar & Logo
navbar_html = """<div class="nav-container">
<div class="brand-wrapper">
<svg width="38" height="38" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="44" height="44" rx="12" fill="#13070b"/>
<rect x="0.5" y="0.5" width="43" height="43" rx="11.5" stroke="#e11d48" stroke-opacity="0.4"/>
<path d="M12 32V12L22 25L32 12V32" stroke="#fda4af" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="22" cy="30" r="2.2" fill="#fb7185"/>
</svg>
<div>
<div class="brand-name">NOVA</div>
<div style="font-size: 10px; color: #94a3b8; letter-spacing: 0.08em; text-transform: uppercase;">Cognitive Load Operating System</div>
</div>
</div>
<div class="status-badge">● Engine Active</div>
</div>"""

st.markdown(navbar_html, unsafe_allow_html=True)

if "tasks" not in st.session_state:
  st.session_state.tasks = [
      {
          "title": "Eczane ve İlaç Temini",
          "due": "Yarın 10:00",
          "owner": "Buse",
          "tag": "Lojistik",
      },
      {
          "title": "Mutfak Derin Temizlik",
          "due": "Bugün 20:00",
          "owner": "Hakan",
          "tag": "Ev Düzeni",
      },
      {
          "title": "Aylık Kira & Fatura Masrafları",
          "due": "15 Ekim",
          "owner": "Hakan",
          "tag": "Finans",
      },
  ]

col_left, col_right = st.columns([1.15, 1], gap="large")

with col_left:
  st.markdown(
      """<div class="nova-card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
<div style="font-weight:700; font-size:16px; color:#fff;">NLP Giriş Akışı</div>
<span style="font-size:11px; color:#64748b; font-family:monospace;">v1.4 Neural Parser</span>
</div>""",
      unsafe_allow_html=True,
  )

  input_text = st.text_area(
      label="Mesaj İçeriği",
      label_visibility="collapsed",
      placeholder=(
          "Doğal bir sohbet mesajı girin: 'Buse yarın marketten kahve alabilir"
          " misin, ben de akşam evi toparlarım.'"
      ),
      height=95,
  )

  col_input1, col_input2 = st.columns([1, 1])
  with col_input1:
    actor = st.selectbox(
        "Mesajı İleten:", ["Hakan", "Buse"], label_visibility="collapsed"
    )
  with col_input2:
    sync_button = st.button("Senkronize Et ⚡", use_container_width=True)

  st.markdown("</div>", unsafe_allow_html=True)

  if sync_button and input_text.strip():
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
    elif any(
        w in raw_lower for w in ["market", "kahve", "ekmek", "süt", "sipariş"]
    ):
      detected_task = "Haftalık Market Tedariği"
      category = "Lojistik"
    elif any(w in raw_lower for w in ["fatura", "kira", "ödeme", "kart"]):
      detected_task = "Bütçe ve Fatura Denkleştirme"
      category = "Finans"
    elif any(
        w in raw_lower for w in ["temizlik", "mutfak", "çöp", "bulaşık", "süpür"]
    ):
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
        "tag": category,
    })
    st.rerun()

  st.markdown("### 📋 Aktif Zihinsel Envanter")
  for t in st.session_state.tasks:
    card_html = f"""<div class="nova-card" style="padding:16px 20px; margin-bottom:12px;">
<div style="display:flex; justify-content:space-between; align-items:flex-start;">
<div>
<div style="font-weight:600; font-size:15px; color:#f8fafc; margin-bottom:6px;">{t['title']}</div>
<div style="font-size:12px; color:#94a3b8;">⏱️ {t['due']} &nbsp;•&nbsp; 👤 <b>{t['owner']}</b></div>
</div>
<span class="tag-badge">{t['tag']}</span>
</div>
</div>"""
    st.markdown(card_html, unsafe_allow_html=True)

with col_right:
  st.markdown("### ⚖️ Yük Denge Analitiği")

  total_tasks = len(st.session_state.tasks)
  hakan_tasks = sum(1 for t in st.session_state.tasks if t["owner"] == "Hakan")
  buse_tasks = sum(1 for t in st.session_state.tasks if t["owner"] == "Buse")

  hakan_ratio = (
      round((hakan_tasks / total_tasks * 100)) if total_tasks > 0 else 50
  )
  buse_ratio = 100 - hakan_ratio if total_tasks > 0 else 50

  st.markdown(
      """<div class="nova-card">
<div style="font-size:12px; font-weight:700; color:#fb7185; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:16px;">
Bilişsel Efor İndeksi
</div>""",
      unsafe_allow_html=True,
  )

  m1, m2 = st.columns(2)
  with m1:
    st.metric(
        label="Hakan Sorumluluğu",
        value=f"%{hakan_ratio}",
        delta=f"{hakan_tasks} görev",
    )
  with m2:
    st.metric(
        label="Buse Sorumluluğu",
        value=f"%{buse_ratio}",
        delta=f"{buse_tasks} görev",
    )

  st.progress(hakan_ratio / 100)
  st.markdown("</div>", unsafe_allow_html=True)

  status_text = (
      "Sistem şu anda dengeli bir bilişsel iş yükü dağılımı öngörüyor."
      if abs(hakan_ratio - buse_ratio) <= 15
      else (
          "Zihinsel yük dağılımında sapma tespit edildi. Görevlerin doğal"
          " aktarımla dengelenmesi önerilir."
      )
  )

  breakdown_html = f"""<div class="nova-card">
<div style="font-size:13px; font-weight:700; color:#f1f5f9; margin-bottom:8px;">Haftalık Görünmez Yük Durumu</div>
<div style="font-size:13px; color:#94a3b8; line-height:1.6;">{status_text}</div>
</div>"""
  st.markdown(breakdown_html, unsafe_allow_html=True)
