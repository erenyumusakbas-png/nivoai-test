import streamlit as st
import random

st.set_page_config(
    page_title="NIVO — Cognitive Balance OS",
    page_icon="⚖️️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# NIVO Su Terazisi Logosu (Base64'e gerek kalmayan kusursuz SVG)
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

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', -apple-system, sans-serif !important; }
.stApp { background-color: #0f1217 !important; color: #e2e8f0 !important; }
#MainMenu, header, footer {visibility: hidden; display: none;}
.block-container { padding-top: 1.2rem !important; padding-bottom: 2rem !important; max-width: 1100px !important; }

/* Antrasit Kartlar */
.nivo-card { background-color: #171b22 !important; border: 1px solid #27303f !important; border-radius: 12px !important; padding: 16px 18px !important; margin-bottom: 12px !important; transition: border-color 0.2s ease;}
.nivo-card:hover { border-color: #384558 !important; }

/* Formlar */
.stTextArea textarea { background-color: #101319 !important; color: #f1f5f9 !important; border: 1px solid #27303f !important; border-radius: 10px !important; font-size: 13.5px !important; }
.stSelectbox div[data-baseweb="select"] > div { background-color: #101319 !important; border: 1px solid #27303f !important; border-radius: 10px !important; color: #f1f5f9 !important; }
div.stButton > button { background-color: #242c38 !important; color: #f8fafc !important; border: 1px solid #384558 !important; border-radius: 10px !important; font-weight: 600 !important; font-size: 13px !important; padding: 0.5rem 1rem !important; }
div.stButton > button:hover { background-color: #2d3746 !important; border-color: #4b5c75 !important; color: #ffffff !important; }
.btn-quick { font-size: 11px !important; padding: 2px 8px !important; }

/* Etiketler (Badges) */
.badge-category { background-color: #101319; border: 1px solid #27303f; color: #94a3b8; border-radius: 6px; padding: 3px 8px; font-size: 10.5px; font-weight: 600; }
.badge-mental { background-color: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.25); color: #38bdf8; border-radius: 6px; padding: 3px 8px; font-size: 10.5px; font-weight: 600; }
.badge-phys { background-color: rgba(148, 163, 184, 0.1); border: 1px solid rgba(148, 163, 184, 0.2); color: #cbd5e1; border-radius: 6px; padding: 3px 8px; font-size: 10.5px; font-weight: 600; }
.badge-alert { background-color: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); color: #f87171; border-radius: 6px; padding: 3px 8px; font-size: 10.5px; font-weight: 700; display: inline-block; margin-top:4px;}
.badge-sync { font-size:10px; color:#10b981; background:rgba(16,185,129,0.1); padding:2px 6px; border-radius:4px; border:1px solid rgba(16,185,129,0.2); }

/* Metrikler */
.metric-tile { background: #101319; border: 1px solid #27303f; border-radius: 10px; padding: 12px 14px; }
.metric-label { font-size: 10.5px; font-weight: 600; color: #8b9bb4; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px; }
.metric-val { font-size: 22px; font-weight: 700; color: #f8fafc; display:flex; align-items:baseline; gap:6px;}
.progress-track { width: 100%; height: 8px; background: #101319; border-radius: 99px; overflow: hidden; display: flex; margin-top: 12px; border: 1px solid #27303f; }
</style>""", unsafe_allow_html=True)

# Üst Bar
head_col1, head_col2, head_col3 = st.columns([0.65, 5, 2.5])
with head_col1: st.image(LOGO_SVG, width=46)
with head_col2:
    st.markdown("""<div style="display:flex; flex-direction:column; justify-content:center; height:46px;">
<div style="font-size:22px; font-weight:800; letter-spacing:0.18em; color:#ffffff; line-height:1;">NIVO</div>
<div style="font-size:9.5px; color:#8b9bb4; letter-spacing:0.08em; text-transform:uppercase; font-weight:600; margin-top:3px;">Cognitive Balance Operating System</div>
</div>""", unsafe_allow_html=True)
with head_col3:
    st.markdown("""<div style="display:flex; justify-content:flex-end; align-items:center; height:46px; gap:8px;">
<div style="background:#171b22; border:1px solid #27303f; color:#94a3b8; padding:5px 10px; border-radius:99px; font-size:11px; font-weight:600; display:flex; align-items:center; gap:6px;"><span style="width:6px; height:6px; background:#f59e0b; border-radius:50%;"></span> Streak: 12 Gün</div>
<div style="background:#171b22; border:1px solid #27303f; color:#94a3b8; padding:5px 10px; border-radius:99px; font-size:11px; font-weight:600; display:flex; align-items:center; gap:6px;"><span style="width:6px; height:6px; background:#10b981; border-radius:50%;"></span> Core Online</div>
</div>""", unsafe_allow_html=True)

st.write("")

# v5 Görev State Yönetimi (Sıfırdan temiz veritabanı simülasyonu)
if "tasks_v5" not in st.session_state:
    st.session_state.tasks_v5 = [
        {"title": "Kedi Aşı Takvimi & Veteriner", "due": "Salı 14:00", "owner": "Buse", "tag": "Evcil Hayvan", "weight": 3, "kind": "Zihinsel", "est": "45 Dk", "sync": True, "alert": ""},
        {"title": "Araç Sigorta Poliçeleri Karşılaştırma", "due": "18 Ekim", "owner": "Hakan", "tag": "Finans", "weight": 3, "kind": "Zihinsel", "est": "1.5 Saat", "sync": False, "alert": ""},
        {"title": "Haftalık Beslenme & Taze Sebze Tedariği", "due": "Bu Akşam", "owner": "Hakan", "tag": "Lojistik", "weight": 2, "kind": "Fiziksel", "est": "40 Dk", "sync": True, "alert": ""},
    ]

if "sample_v5" not in st.session_state:
    st.session_state.sample_v5 = ""

col_left, col_right = st.columns([1.2, 1], gap="medium")

with col_left:
    st.markdown("""<div class="nivo-card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
<div style="font-weight:600; font-size:13.5px; color:#f8fafc;">WhatsApp NLP Motoru & Duygu Analizi</div>
<span style="font-size:10px; color:#64748b; font-family:monospace;">Engine v5.2</span>
</div>""", unsafe_allow_html=True)

    c_s1, c_s2, c_s3 = st.columns(3)
    with c_s1:
        if st.button("🚨 Tükenmişlik Örneği", use_container_width=True):
            st.session_state.sample_v5 = "Yine mutfak darmadağın kalmış, her akşam ben toplamaktan gerçekten çok yoruldum artık."
            st.rerun()
    with c_s2:
        if st.button("🔧 Rutin Kriz Örneği", use_container_width=True):
            st.session_state.sample_v5 = "Kombi yine su akıtıyor, yarın sabahtan acil usta bulup başında durman lazım."
            st.rerun()
    with c_s3:
        if st.button("🛒 Standart Örnek", use_container_width=True):
            st.session_state.sample_v5 = "Buse gelirken eczaneden ilacımı alır mısın rica etsem?"
            st.rerun()

    input_text = st.text_area(
        label="Mesaj",
        label_visibility="collapsed",
        value=st.session_state.sample_v5,
        placeholder="Doğal bir sohbet kopyalayın...",
        height=75
    )

    c1, c2, c3 = st.columns([1.5, 1, 1.2])
    with c1:
        actor = st.selectbox("İleten (Sitem Sahibi):", ["Hakan", "Buse"], label_visibility="collapsed")
    with c2:
        do_sync = st.checkbox("Takvime İşle", value=True)
    with c3:
        sync_btn = st.button("Senkronize Et ⚡", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Parser & Sentiment Analyzer Logic
    if sync_btn and input_text.strip():
        txt = input_text.lower()
        title = "Rutin Koordinasyon"
        category = "Genel"
        w = 1
        kind = "Fiziksel"
        est_time = "15 Dk"
        alert_msg = ""

        # Tükenmişlik (Burnout) Check
        stress_words = ["yine", "hep", "yoruldum", "bıktım", "tek başıma", "sürekli", "artık"]
        is_stressed = any(sw in txt for sw in stress_words)
        if is_stressed:
            alert_msg = "⚠️ Tükenmişlik Sinyali Algılandı"
            w += 1 # Stresli işin ağırlığı artar

        if any(k in txt for k in ["veteriner", "kedi", "mama", "aşı"]):
            title, category, w, kind, est_time = "Evcil Hayvan Sağlık Takibi", "Evcil Hayvan", 3, "Zihinsel", "45 Dk"
        elif any(k in txt for k in ["fatura", "kira", "sigorta", "ödeme"]):
            title, category, w, kind, est_time = "Finans & Bütçe Yönetimi", "Finans", 3, "Zihinsel", "30 Dk"
        elif any(k in txt for k in ["market", "kahve", "eczane", "ilaç"]):
            title, category, w, kind, est_time = "Dış İkmal & Lojistik", "Lojistik", 2, "Fiziksel", "1 Saat"
        elif any(k in txt for k in ["usta", "servis", "kombi", "tamir"]):
            title, category, w, kind, est_time = "Teknik Bakım Koordinasyonu", "Ev Düzeni", 3, "Zihinsel", "2.5 Saat"
        elif any(k in txt for k in ["temizlik", "çöp", "bulaşık", "mutfak"]):
            title, category, w, kind, est_time = "Fiziksel Ev Hijyeni", "Ev Düzeni", 2, "Fiziksel", "1 Saat"
        else:
            title = input_text[:30].strip() + "..."

        due = "Yarın" if "yarın" in txt else ("Bu Akşam" if "akşam" in txt else "Yakında")
        
        # Eğer mesajda stres varsa, owner o kişi olmasın, karşı tarafa önerilsin.
        assigned_owner = actor
        if is_stressed:
            assigned_owner = "Buse" if actor == "Hakan" else "Hakan"

        st.session_state.tasks_v5.insert(0, {
            "title": title,
            "due": due,
            "owner": assigned_owner,
            "tag": category,
            "weight": w,
            "kind": kind,
            "est": est_time,
            "sync": do_sync,
            "alert": alert_msg
        })
        st.session_state.sample_v5 = ""
        st.rerun()

    # Görev Listesi Render
    st.markdown("<div style='font-size:12.5px; font-weight:700; color:#8b9bb4; margin:16px 0 8px 2px;'>📋 AKTİF ZİHİNSEL & FİZİKSEL ENVANTER</div>", unsafe_allow_html=True)

    if st.session_state.tasks_v5:
        for idx, t in enumerate(list(st.session_state.tasks_v5)):
            col_t1, col_t2, col_t3 = st.columns([4.8, 1.2, 1.2])
            with col_t1:
                k_badge = f'<span class="badge-mental">🧠 {t["kind"]}</span>' if t["kind"] == "Zihinsel" else f'<span class="badge-phys">🛠️ {t["kind"]}</span>'
                s_badge = f'<span class="badge-sync">🗓️ Sync</span>' if t.get("sync") else ""
                a_badge = f'<div class="badge-alert">{t["alert"]}</div>' if t.get("alert") else ""
                stars = "⚡" * t["weight"]
                
                item_html = f"""<div class="nivo-card" style="margin-bottom:8px; padding:14px 16px;">
<div style="display:flex; justify-content:space-between; align-items:flex-start;">
<div>
<div style="font-weight:600; font-size:13.5px; color:#f1f5f9; margin-bottom:4px;">{t['title']}</div>
<div style="font-size:11.5px; color:#8b9bb4; margin-bottom:6px;">⏱️ {t['due']} &nbsp;•&nbsp; 👤 <b>{t['owner']}</b> &nbsp;•&nbsp; ⏳ {t.get("est", "N/A")}</div>
<div style="display:flex; gap:6px; align-items:center;">
{k_badge} <span class="badge-category">{t['tag']}</span> <span style="font-size:10px;" title="Zorluk Derecesi">{stars}</span> {s_badge}
</div>
{a_badge}
</div>
</div>
</div>"""
                st.markdown(item_html, unsafe_allow_html=True)
            with col_t2:
                other_person = "Buse" if t["owner"] == "Hakan" else "Hakan"
                if st.button("Devret ⇄", key=f"swap_{idx}"):
                    st.session_state.tasks_v5[idx]["owner"] = other_person
                    st.rerun()
            with col_t3:
                if st.button("Bitir ✓", key=f"done_{idx}"):
                    st.session_state.tasks_v5.pop(idx)
                    st.rerun()
    else:
        st.info("Harika, sistem dengede. Aktif görev bulunmuyor.")

with col_right:
    st.markdown("<div style='font-size:12.5px; font-weight:700; color:#8b9bb4; margin:0 0 8px 2px;'>⚖️ BİLİŞSEL YÜK ANALİTİĞİ</div>", unsafe_allow_html=True)

    h_weight = sum(t["weight"] for t in st.session_state.tasks_v5 if t["owner"] == "Hakan")
    b_weight = sum(t["weight"] for t in st.session_state.tasks_v5 if t["owner"] == "Buse")
    tot_weight = h_weight + b_weight

    h_ratio = round((h_weight / tot_weight * 100)) if tot_weight > 0 else 50
    b_ratio = 100 - h_ratio if tot_weight > 0 else 50

    h_mental = sum(1 for t in st.session_state.tasks_v5 if t["owner"] == "Hakan" and t["kind"] == "Zihinsel")
    b_mental = sum(1 for t in st.session_state.tasks_v5 if t["owner"] == "Buse" and t["kind"] == "Zihinsel")

    card_stat = f"""<div class="nivo-card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
<div style="font-size:10.5px; font-weight:700; color:#8b9bb4; letter-spacing:0.06em; text-transform:uppercase;">Bilişsel Efor İndeksi</div>
<span style="font-size:10px; color:#38bdf8; font-family:monospace;">Realtime Ratio</span>
</div>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
<div class="metric-tile">
<div class="metric-label">Hakan Toplam Yük</div>
<div class="metric-val">%{h_ratio} <span style="font-size:11px; color:#64748b; font-weight:500;">({h_weight} pts)</span></div>
<div style="font-size:10.5px; color:#38bdf8; margin-top:4px;">🧠 {h_mental} Zihinsel Yük</div>
</div>
<div class="metric-tile">
<div class="metric-label">Buse Toplam Yük</div>
<div class="metric-val">%{b_ratio} <span style="font-size:11px; color:#64748b; font-weight:500;">({b_weight} pts)</span></div>
<div style="font-size:10.5px; color:#38bdf8; margin-top:4px;">🧠 {b_mental} Zihinsel Yük</div>
</div>
</div>
<div class="progress-track">
<div style="width:{h_ratio}%; background:#38bdf8; transition:width 0.4s ease;"></div>
<div style="width:{b_ratio}%; background:#334155; transition:width 0.4s ease;"></div>
</div>
</div>"""
    st.markdown(card_stat, unsafe_allow_html=True)

    # Duygu Analizi / Tükenmişlik Radarı Sonucu
    has_alert = any(t.get("alert") for t in st.session_state.tasks_v5)
    if has_alert:
        radar_title = "🚨 Stres ve Duygu Radarı Aktif"
        radar_msg = "Sistem iletişimde **tükenmişlik ve sitem** tespit etti. Bu durum zihinsel yükün eşitsiz dağıldığının net göstergesidir. Lütfen kriz anındaki görevleri doğrudan diğer partnere devredin."
        radar_border = "border-color: #ef4444;"
    else:
        radar_title = "💚 İletişim Tonu Sağlıklı"
        radar_msg = "Son mesajlarda pasif-agresif veya yorgun bir ton tespit edilmedi. Psikolojik ve zihinsel iletişim akışı sağlıklı devam ediyor."
        radar_border = "border-color: #10b981;"

    st.markdown(f"""<div class="nivo-card" style="border-left: 3px solid transparent; {radar_border}">
<div style="font-weight:600; font-size:12.5px; color:#f8fafc; margin-bottom:4px;">{radar_title}</div>
<div style="font-size:11.5px; color:#8b9bb4; line-height:1.5;">{radar_msg}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("""<div class="nivo-card" style="border-style:dashed;">
<div style="font-weight:600; font-size:11.5px; color:#cbd5e1; margin-bottom:4px;">🛡️ Sıfır Konuşma Saklama Protokolü</div>
<div style="font-size:11px; color:#64748b; line-height:1.45;">Mesajlar RAM'de işlenir ve saniyesinde JSON verisine çevrilip imha edilir. Gizlilik esastır.</div>
</div>""", unsafe_allow_html=True)
