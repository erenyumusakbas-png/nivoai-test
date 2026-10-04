import streamlit as st

st.set_page_config(
    page_title="NIVO — Cognitive Balance OS",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Kesin ve Kusursuz Görünen SVG Logo (Su Terazisi & Denge Konsepti)
LOGO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="bgG" x1="0" y1="0" x2="100" y2="100" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#1e2430"/>
      <stop offset="100%" stop-color="#0c0e14"/>
    </linearGradient>
    <linearGradient id="beamG" x1="20" y1="50" x2="80" y2="50" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.3"/>
    </linearGradient>
  </defs>
  <!-- Titanyum Çerçeve -->
  <rect x="2" y="2" width="96" height="96" rx="24" fill="url(#bgG)" stroke="#334155" stroke-width="3"/>
  <!-- Denge Ekseni (Su Terazisi Tüpü) -->
  <rect x="18" y="42" width="64" height="16" rx="8" fill="#131922" stroke="#475569" stroke-width="2.5"/>
  <!-- Neon Denge Sıvısı ve Hava Kabarcığı -->
  <line x1="26" y1="50" x2="74" y2="50" stroke="url(#beamG)" stroke-width="3" stroke-linecap="round"/>
  <circle cx="50" cy="50" r="5.5" fill="#38bdf8"/>
  <circle cx="50" cy="50" r="2.2" fill="#ffffff"/>
  <!-- Hassas Denge Çizgileri -->
  <line x1="42" y1="36" x2="42" y2="42" stroke="#64748b" stroke-width="2" stroke-linecap="round"/>
  <line x1="58" y1="36" x2="58" y2="42" stroke="#64748b" stroke-width="2" stroke-linecap="round"/>
</svg>"""

# Arayüz Stili
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, sans-serif !important;
}

.stApp {
    background-color: #0f1217 !important;
    color: #e2e8f0 !important;
}

#MainMenu, header, footer {visibility: hidden; display: none;}
.block-container {
    padding-top: 1.2rem !important;
    padding-bottom: 2rem !important;
    max-width: 1040px !important;
}

.nivo-card {
    background-color: #171b22 !important;
    border: 1px solid #27303f !important;
    border-radius: 12px !important;
    padding: 16px 18px !important;
    margin-bottom: 12px !important;
}

.stTextArea textarea {
    background-color: #101319 !important;
    color: #f1f5f9 !important;
    border: 1px solid #27303f !important;
    border-radius: 10px !important;
    font-size: 13.5px !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: #101319 !important;
    border: 1px solid #27303f !important;
    border-radius: 10px !important;
    color: #f1f5f9 !important;
}

div.stButton > button {
    background-color: #242c38 !important;
    color: #f8fafc !important;
    border: 1px solid #384558 !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 13.5px !important;
    padding: 0.6rem 1.2rem !important;
}

div.stButton > button:hover {
    background-color: #2d3746 !important;
    border-color: #4b5c75 !important;
    color: #ffffff !important;
}

.badge-category {
    background-color: #101319;
    border: 1px solid #27303f;
    color: #94a3b8;
    border-radius: 6px;
    padding: 3px 8px;
    font-size: 10.5px;
    font-weight: 600;
}

.metric-tile {
    background: #101319;
    border: 1px solid #27303f;
    border-radius: 10px;
    padding: 12px 14px;
}

.metric-label {
    font-size: 10.5px;
    font-weight: 600;
    color: #8b9bb4;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 4px;
}

.metric-val {
    font-size: 22px;
    font-weight: 700;
    color: #f8fafc;
}

.progress-track {
    width: 100%;
    height: 8px;
    background: #101319;
    border-radius: 99px;
    overflow: hidden;
    display: flex;
    margin-top: 12px;
    border: 1px solid #27303f;
}
</style>""", unsafe_allow_html=True)

# Üst Bar - Streamlit Yerel Bileşenleriyle Hizalanmış
head_col1, head_col2, head_col3 = st.columns([0.65, 5, 2])

with head_col1:
    st.image(LOGO_SVG, width=44)

with head_col2:
    st.markdown("""<div style="display:flex; flex-direction:column; justify-content:center; height:44px;">
<div style="font-size:22px; font-weight:800; letter-spacing:0.18em; color:#ffffff; line-height:1;">NIVO</div>
<div style="font-size:9.5px; color:#8b9bb4; letter-spacing:0.08em; text-transform:uppercase; font-weight:600; margin-top:3px;">Cognitive Balance Operating System</div>
</div>""", unsafe_allow_html=True)

with head_col3:
    st.markdown("""<div style="display:flex; justify-content:flex-end; align-items:center; height:44px;">
<div style="background:#171b22; border:1px solid #27303f; color:#94a3b8; padding:5px 12px; border-radius:99px; font-size:11px; font-weight:600; display:flex; align-items:center; gap:6px;">
<span style="width:6px; height:6px; background:#10b981; border-radius:50%;"></span> E2EE Active
</div>
</div>""", unsafe_allow_html=True)

st.write("") # Dikey boşluk

# Görev Listesi
if "tasks_v3" not in st.session_state:
    st.session_state.tasks_v3 = [
        {"title": "Veteriner Randevusu & Aşı Takibi", "due": "Salı 14:00", "owner": "Buse", "tag": "Evcil Hayvan", "weight": 3},
        {"title": "Araç & Konut Sigortası Yenileme", "due": "18 Ekim", "owner": "Hakan", "tag": "Finans", "weight": 3},
        {"title": "Haftalık Market & Beslenme Planı", "due": "Bu Akşam", "owner": "Buse", "tag": "Lojistik", "weight": 2},
        {"title": "Kombi Bakımı ve Yetkili Servis", "due": "Cuma", "owner": "Hakan", "tag": "Ev Düzeni", "weight": 2},
    ]

col_left, col_right = st.columns([1.15, 1], gap="medium")

with col_left:
    st.markdown("""<div class="nivo-card">
<div style="font-weight:600; font-size:13.5px; color:#f8fafc; margin-bottom:10px;">WhatsApp Girdisi</div>""", unsafe_allow_html=True)

    input_text = st.text_area(
        label="Mesaj",
        label_visibility="collapsed",
        placeholder="Mesaj yapıştırın: 'Buse yarın marketten kahve alır mısın, ben de akşam mutfağı hallederim.'",
        height=80
    )

    c1, c2 = st.columns([1, 1])
    with c1:
        actor = st.selectbox("İleten:", ["Hakan", "Buse"], label_visibility="collapsed")
    with c2:
        sync_btn = st.button("Senkronize Et ⚡", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if sync_btn and input_text.strip():
        txt = input_text.lower()
        title = "Rutin Koordinasyon"
        category = "Genel"
        w = 1

        if any(k in txt for k in ["veteriner", "kedi", "mama", "aşı"]):
            title = "Evcil Hayvan Bakımı"
            category = "Evcil Hayvan"
            w = 3
        elif any(k in txt for k in ["fatura", "kira", "sigorta", "ödeme", "kart"]):
            title = "Finans & Bütçe Yönetimi"
            category = "Finans"
            w = 3
        elif any(k in txt for k in ["market", "kahve", "sipariş", "yemek", "su"]):
            title = "Market & Ev Tedariği"
            category = "Lojistik"
            w = 2
        elif any(k in txt for k in ["temizlik", "kombi", "servis", "tamir", "çöp"]):
            title = "Ev Hijyeni & Onarım"
            category = "Ev Düzeni"
            w = 2
        else:
            title = input_text[:35].strip() + "..."

        due = "Yarın" if "yarın" in txt else ("Bu Akşam" if "akşam" in txt else "Yakında")

        st.session_state.tasks_v3.insert(0, {
            "title": title,
            "due": due,
            "owner": actor,
            "tag": category,
            "weight": w
        })
        st.rerun()

    st.markdown("<div style='font-size:13px; font-weight:700; color:#8b9bb4; margin:16px 0 8px 2px;'>AKTİF ZİHİNSEL ENVANTER</div>", unsafe_allow_html=True)

    if st.session_state.tasks_v3:
        for idx, t in enumerate(list(st.session_state.tasks_v3)):
            col_t1, col_t2 = st.columns([5.5, 1])
            with col_t1:
                item_html = f"""<div class="nivo-card" style="margin-bottom:8px; padding:12px 16px;">
<div style="display:flex; justify-content:space-between; align-items:flex-start;">
<div>
<div style="font-weight:600; font-size:13.5px; color:#f1f5f9; margin-bottom:4px;">{t['title']}</div>
<div style="font-size:11.5px; color:#8b9bb4;">⏱️ {t['due']} &nbsp;•&nbsp; 👤 <b>{t['owner']}</b></div>
</div>
<span class="badge-category">{t['tag']}</span>
</div>
</div>"""
                st.markdown(item_html, unsafe_allow_html=True)
            with col_t2:
                if st.button("Bitir", key=f"btn_done_{idx}", help="Görevi tamamla"):
                    st.session_state.tasks_v3.pop(idx)
                    st.rerun()
    else:
        st.info("Tüm sorumluluklar tamamlandı, zihinsel yük sıfırlandı.")

with col_right:
    st.markdown("<div style='font-size:13px; font-weight:700; color:#8b9bb4; margin:0 0 8px 2px;'>BİLİŞSEL YÜK ANALİTİĞİ</div>", unsafe_allow_html=True)

    h_weight = sum(t.get("weight", 1) for t in st.session_state.tasks_v3 if t["owner"] == "Hakan")
    b_weight = sum(t.get("weight", 1) for t in st.session_state.tasks_v3 if t["owner"] == "Buse")
    tot_weight = h_weight + b_weight

    h_ratio = round((h_weight / tot_weight * 100)) if tot_weight > 0 else 50
    b_ratio = 100 - h_ratio if tot_weight > 0 else 50

    card_stat = f"""<div class="nivo-card">
<div style="font-size:10.5px; font-weight:700; color:#8b9bb4; letter-spacing:0.06em; text-transform:uppercase; margin-bottom:12px;">
Ağırlıklı Efor Dağılımı
</div>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
<div class="metric-tile">
<div class="metric-label">Hakan Sorumluluğu</div>
<div class="metric-val">%{h_ratio} <span style="font-size:11px; color:#64748b; font-weight:500;">({h_weight} puan)</span></div>
</div>
<div class="metric-tile">
<div class="metric-label">Buse Sorumluluğu</div>
<div class="metric-val">%{b_ratio} <span style="font-size:11px; color:#64748b; font-weight:500;">({b_weight} puan)</span></div>
</div>
</div>
<div class="progress-track">
<div style="width:{h_ratio}%; background:#475569;"></div>
<div style="width:{b_ratio}%; background:#242c38;"></div>
</div>
</div>"""
    st.markdown(card_stat, unsafe_allow_html=True)

    if abs(h_ratio - b_ratio) <= 15:
        msg = "Zihinsel efor dengede. İki taraf da eşit yük taşıyor."
    elif h_ratio > b_ratio:
        msg = "Hakan üzerinde planlama yükü daha fazla. Bir sonraki görevin devri önerilir."
    else:
        msg = "Buse üzerinde takip yükü yoğunlaşmış durumda. Görevlerin dengelenmesi önerilir."

    st.markdown(f"""<div class="nivo-card">
<div style="font-weight:600; font-size:12.5px; color:#f8fafc; margin-bottom:4px;">Denge Önerisi</div>
<div style="font-size:12px; color:#8b9bb4; line-height:1.5;">{msg}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("""<div class="nivo-card" style="border-style:dashed;">
<div style="font-weight:600; font-size:11.5px; color:#cbd5e1; margin-bottom:4px;">🛡️ Sıfır Konuşma Saklama</div>
<div style="font-size:11px; color:#64748b; line-height:1.45;">WhatsApp mesajları işlenir işlenmez silinir, sunucuda metin saklanmaz.</div>
</div>""", unsafe_allow_html=True)
