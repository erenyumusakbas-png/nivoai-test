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
  <rect x="2" y="2" width="96" height="96" rx="24" fill="url(#bgG)" stroke="#334155" stroke-width="3"/>
  <rect x="18" y="42" width="64" height="16" rx="8" fill="#131922" stroke="#475569" stroke-width="2.5"/>
  <line x1="26" y1="50" x2="74" y2="50" stroke="url(#beamG)" stroke-width="3" stroke-linecap="round"/>
  <circle cx="50" cy="50" r="5.5" fill="#38bdf8"/>
  <circle cx="50" cy="50" r="2.2" fill="#ffffff"/>
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
    max-width: 1060px !important;
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
    font-size: 13px !important;
    padding: 0.5rem 1rem !important;
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

.badge-type-mental {
    background-color: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.25);
    color: #38bdf8;
    border-radius: 6px;
    padding: 3px 8px;
    font-size: 10.5px;
    font-weight: 600;
}

.badge-type-phys {
    background-color: rgba(148, 163, 184, 0.1);
    border: 1px solid rgba(148, 163, 184, 0.2);
    color: #cbd5e1;
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

# Üst Bar
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
<span style="width:6px; height:6px; background:#10b981; border-radius:50%;"></span> Zero-Retention Core
</div>
</div>""", unsafe_allow_html=True)

st.write("")

# Gelişmiş Görev Havuzu State Yapısı
if "tasks_v4" not in st.session_state:
    st.session_state.tasks_v4 = [
        {"title": "Kedinin Aşı Takvimi & Veteriner Randevusu", "due": "Salı 14:00", "owner": "Buse", "tag": "Evcil Hayvan", "weight": 3, "kind": "Zihinsel"},
        {"title": "Araç & Konut Sigortası Teklifleri Karşılaştırma", "due": "18 Ekim", "owner": "Hakan", "tag": "Finans", "weight": 3, "kind": "Zihinsel"},
        {"title": "Haftalık Market Tedariği ve Sebze Alışverişi", "due": "Bu Akşam", "owner": "Hakan", "tag": "Lojistik", "weight": 2, "kind": "Fiziksel"},
        {"title": "Kombi Yıllık Bakımı Yetkili Servis Arama", "due": "Cuma 11:00", "owner": "Buse", "tag": "Ev Düzeni", "weight": 2, "kind": "Zihinsel"},
        {"title": "Balkon ve Mutfak Derin Temizliği", "due": "Hafta Sonu", "owner": "Hakan", "tag": "Ev Düzeni", "weight": 1, "kind": "Fiziksel"},
    ]

if "sample_msg" not in st.session_state:
    st.session_state.sample_msg = ""

col_left, col_right = st.columns([1.18, 1], gap="medium")

with col_left:
    st.markdown("""<div class="nivo-card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
<div style="font-weight:600; font-size:13.5px; color:#f8fafc;">WhatsApp Doğal Dil Entegrasyonu</div>
<span style="font-size:10px; color:#64748b; font-family:monospace;">RAM Parse v2.1</span>
</div>""", unsafe_allow_html=True)

    # Hızlı Senaryo Şablonları Çipleri
    st.markdown("<div style='font-size:11px; color:#8b9bb4; margin-bottom:6px;'>Hızlı WhatsApp Örnekleri (Tıkla ve Doldur):</div>", unsafe_allow_html=True)
    c_s1, c_s2, c_s3 = st.columns(3)
    with c_s1:
        if st.button("🐱 Mama & Veteriner", use_container_width=True):
            st.session_state.sample_msg = "Buse yarın kedinin mamasını sipariş edebilir misin, aşı günü de yaklaşıyor."
            st.rerun()
    with c_s2:
        if st.button("💳 Kira & Faturalar", use_container_width=True):
            st.session_state.sample_msg = "Hakan bu ayki aidat ve internet faturasını yatırmayı unutma lütfen."
            st.rerun()
    with c_s3:
        if st.button("🔧 Kombi / Usta", use_container_width=True):
            st.session_state.sample_msg = "Hakan kombiden ses geliyor yarın servis için bir usta bulabilir misin?"
            st.rerun()

    input_text = st.text_area(
        label="Mesaj",
        label_visibility="collapsed",
        value=st.session_state.sample_msg,
        placeholder="Mesaj yapıştırın: 'Buse yarın marketten kahve alır mısın, ben de akşam mutfağı hallederim.'",
        height=75
    )

    c1, c2 = st.columns([1, 1])
    with c1:
        actor = st.selectbox("Mesaj Sahibi:", ["Hakan", "Buse"], label_visibility="collapsed")
    with c2:
        sync_btn = st.button("Senkronize Et ⚡", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Görev Çıkarma ve Zihinsel/Fiziksel Tipi Belirleme Mantığı
    if sync_btn and input_text.strip():
        txt = input_text.lower()
        title = "Rutin Koordinasyon"
        category = "Genel"
        w = 1
        kind = "Fiziksel"

        if any(k in txt for k in ["veteriner", "kedi", "mama", "aşı"]):
            title = "Evcil Hayvan Sağlık & Tedarik"
            category = "Evcil Hayvan"
            w = 3
            kind = "Zihinsel"
        elif any(k in txt for k in ["fatura", "kira", "sigorta", "ödeme", "kart", "aidat"]):
            title = "Finans & Bütçe Yönetimi"
            category = "Finans"
            w = 3
            kind = "Zihinsel"
        elif any(k in txt for k in ["market", "kahve", "sipariş", "yemek", "su"]):
            title = "Market & Ev İkmal Lojistiği"
            category = "Lojistik"
            w = 2
            kind = "Fiziksel"
        elif any(k in txt for k in ["usta", "servis", "kombi", "tamir"]):
            title = "Teknik Servis & Bakım Koordinasyonu"
            category = "Ev Düzeni"
            w = 2
            kind = "Zihinsel"
        elif any(k in txt for k in ["temizlik", "çöp", "bulaşık", "süpür"]):
            title = "Ev Hijyeni ve Fiziksel Düzen"
            category = "Ev Düzeni"
            w = 1
            kind = "Fiziksel"
        else:
            title = input_text[:35].strip() + "..."

        due = "Yarın" if "yarın" in txt else ("Bu Akşam" if "akşam" in txt else "Yakında")

        st.session_state.tasks_v4.insert(0, {
            "title": title,
            "due": due,
            "owner": actor,
            "tag": category,
            "weight": w,
            "kind": kind
        })
        st.session_state.sample_msg = ""
        st.rerun()

    # Görev Listesi ve Etkileşimler
    st.markdown("<div style='font-size:13px; font-weight:700; color:#8b9bb4; margin:16px 0 8px 2px;'>📋 AKTİF ZİHİNSEL ENVANTER</div>", unsafe_allow_html=True)

    if st.session_state.tasks_v4:
        for idx, t in enumerate(list(st.session_state.tasks_v4)):
            col_t1, col_t2, col_t3 = st.columns([5.2, 1.1, 1.1])
            with col_t1:
                kind_badge = f'<span class="badge-type-mental">🧠 {t["kind"]}</span>' if t["kind"] == "Zihinsel" else f'<span class="badge-type-phys">🛠️ {t["kind"]}</span>'
                stars = "⚡" * t["weight"]
                item_html = f"""<div class="nivo-card" style="margin-bottom:8px; padding:12px 16px;">
<div style="display:flex; justify-content:space-between; align-items:flex-start;">
<div>
<div style="font-weight:600; font-size:13.5px; color:#f1f5f9; margin-bottom:4px;">{t['title']}</div>
<div style="font-size:11.5px; color:#8b9bb4;">⏱️ {t['due']} &nbsp;•&nbsp; 👤 <b>{t['owner']}</b> &nbsp;•&nbsp; <span title="Bilişsel Efor Derecesi">{stars}</span></div>
</div>
<div style="display:flex; gap:6px; align-items:center;">
{kind_badge}
<span class="badge-category">{t['tag']}</span>
</div>
</div>
</div>"""
                st.markdown(item_html, unsafe_allow_html=True)
            with col_t2:
                # Sorumluluk Devretme Butonu
                other_person = "Buse" if t["owner"] == "Hakan" else "Hakan"
                if st.button("Devret ⇄", key=f"btn_swap_{idx}", help=f"Sorumluluğu {other_person}'e aktar"):
                    st.session_state.tasks_v4[idx]["owner"] = other_person
                    st.rerun()
            with col_t3:
                # Tamamlama Butonu
                if st.button("Bitir ✓", key=f"btn_done_{idx}", help="Görevi tamamla"):
                    st.session_state.tasks_v4.pop(idx)
                    st.rerun()
    else:
        st.info("Tüm sorumluluklar tamamlandı! Zihinsel yük sıfırlandı.")

with col_right:
    st.markdown("<div style='font-size:13px; font-weight:700; color:#8b9bb4; margin:0 0 8px 2px;'>⚖️ BİLİŞSEL YÜK ANALİTİĞİ</div>", unsafe_allow_html=True)

    h_weight = sum(t.get("weight", 1) for t in st.session_state.tasks_v4 if t["owner"] == "Hakan")
    b_weight = sum(t.get("weight", 1) for t in st.session_state.tasks_v4 if t["owner"] == "Buse")
    tot_weight = h_weight + b_weight

    h_ratio = round((h_weight / tot_weight * 100)) if tot_weight > 0 else 50
    b_ratio = 100 - h_ratio if tot_weight > 0 else 50

    # Zihinsel (Mental) Yük Oranı Ayrımı
    h_mental = sum(1 for t in st.session_state.tasks_v4 if t["owner"] == "Hakan" and t.get("kind") == "Zihinsel")
    b_mental = sum(1 for t in st.session_state.tasks_v4 if t["owner"] == "Buse" and t.get("kind") == "Zihinsel")

    card_stat = f"""<div class="nivo-card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
<div style="font-size:10.5px; font-weight:700; color:#8b9bb4; letter-spacing:0.06em; text-transform:uppercase;">
Bilişsel Efor İndeksi (Ağırlıklı Puan)
</div>
<span style="font-size:10px; color:#38bdf8; font-family:monospace;">Realtime Ratio</span>
</div>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
<div class="metric-tile">
<div class="metric-label">Hakan Toplam Yük</div>
<div class="metric-val">%{h_ratio} <span style="font-size:11px; color:#64748b; font-weight:500;">({h_weight} pts)</span></div>
<div style="font-size:10.5px; color:#38bdf8; margin-top:4px;">🧠 {h_mental} Zihinsel Takip</div>
</div>
<div class="metric-tile">
<div class="metric-label">Buse Toplam Yük</div>
<div class="metric-val">%{b_ratio} <span style="font-size:11px; color:#64748b; font-weight:500;">({b_weight} pts)</span></div>
<div style="font-size:10.5px; color:#38bdf8; margin-top:4px;">🧠 {b_mental} Zihinsel Takip</div>
</div>
</div>
<div class="progress-track">
<div style="width:{h_ratio}%; background:#38bdf8;"></div>
<div style="width:{b_ratio}%; background:#334155;"></div>
</div>
</div>"""
    st.markdown(card_stat, unsafe_allow_html=True)

    # Akıllı Dengeleme Algoritması Tavsiyesi
    if abs(h_ratio - b_ratio) <= 15:
        msg = "Zihinsel ve fiziksel efor mükemmel dengede. İki taraf da eşit yük taşıyor."
    elif h_ratio > b_ratio:
        msg = "Hakan üzerinde planlama ve takip yükü birikmiş durumda. Bir sonraki zihinsel görevi 'Devret' butonuyla Buse'ye aktarmanız önerilir."
    else:
        msg = "Buse üzerinde görünmez zihinsel yük yoğunlaşmış durumda. Sıradaki organizasyonel eforu Hakan'ın üstlenmesi dengeyi korur."

    st.markdown(f"""<div class="nivo-card">
<div style="font-weight:600; font-size:12.5px; color:#f8fafc; margin-bottom:4px;">Akıllı Dengeleme Önerisi</div>
<div style="font-size:12px; color:#8b9bb4; line-height:1.5;">{msg}</div>
</div>""", unsafe_allow_html=True)

    # Kategori Röntgeni
    tags_count = {}
    for t in st.session_state.tasks_v4:
        tag = t.get("tag", "Genel")
        tags_count[tag] = tags_count.get(tag, 0) + 1

    tags_html = "".join([f"<span class='badge-category' style='margin-right:6px; margin-bottom:4px; display:inline-block;'>{k}: {v}</span>" for k, v in tags_count.items()])
    
    st.markdown(f"""<div class="nivo-card">
<div style="font-weight:600; font-size:12px; color:#cbd5e1; margin-bottom:8px;">Kategori Bazlı Yük Röntgeni</div>
<div>{tags_html}</div>
</div>""", unsafe_allow_html=True)

    # Gizlilik Protokolü
    st.markdown("""<div class="nivo-card" style="border-style:dashed;">
<div style="font-weight:600; font-size:11.5px; color:#cbd5e1; margin-bottom:4px;">🛡️ Sıfır Konuşma Saklama Protokolü</div>
<div style="font-size:11px; color:#64748b; line-height:1.45;">WhatsApp mesajları RAM üzerinde parse edildikten hemen sonra imha edilir; sunucuda asla ham sohbet veya ses verisi saklanmaz.</div>
</div>""", unsafe_allow_html=True)
