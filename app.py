import streamlit as st
import random
import re

st.set_page_config(
    page_title="NIVO — Cognitive Balance OS",
    page_icon="⚖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# NIVO Su Terazisi Logosu
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', -apple-system, sans-serif !important; }
.stApp { background-color: #0f1217 !important; color: #e2e8f0 !important; }
#MainMenu, header, footer {visibility: hidden; display: none;}
.block-container { padding-top: 1.2rem !important; padding-bottom: 2rem !important; max-width: 1140px !important; }

/* Arayüz Kartları */
.nivo-card { background-color: #171b22 !important; border: 1px solid #27303f !important; border-radius: 12px !important; padding: 18px 20px !important; margin-bottom: 12px !important; transition: border-color 0.2s ease, box-shadow 0.2s ease;}
.nivo-card:hover { border-color: #384558 !important; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }

.stTextArea textarea { background-color: #101319 !important; color: #f1f5f9 !important; border: 1px solid #27303f !important; border-radius: 10px !important; font-size: 13.5px !important; padding: 12px !important;}
.stSelectbox div[data-baseweb="select"] > div { background-color: #101319 !important; border: 1px solid #27303f !important; border-radius: 10px !important; color: #f1f5f9 !important; }
div.stButton > button { background-color: #242c38 !important; color: #f8fafc !important; border: 1px solid #384558 !important; border-radius: 10px !important; font-weight: 600 !important; font-size: 13px !important; padding: 0.5rem 1rem !important; }
div.stButton > button:hover { background-color: #2d3746 !important; border-color: #4b5c75 !important; color: #ffffff !important; }

/* Rozetler */
.badge-category { background-color: #101319; border: 1px solid #27303f; color: #94a3b8; border-radius: 6px; padding: 4px 8px; font-size: 10.5px; font-weight: 600; white-space:nowrap; }
.badge-mental { background-color: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.25); color: #38bdf8; border-radius: 6px; padding: 4px 8px; font-size: 10.5px; font-weight: 600; white-space:nowrap;}
.badge-phys { background-color: rgba(148, 163, 184, 0.1); border: 1px solid rgba(148, 163, 184, 0.2); color: #cbd5e1; border-radius: 6px; padding: 4px 8px; font-size: 10.5px; font-weight: 600; white-space:nowrap;}
.badge-alert { background-color: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); color: #f87171; border-radius: 6px; padding: 4px 8px; font-size: 10.5px; font-weight: 700; display: inline-block; margin-top:8px;}
.badge-sync { font-size:10.5px; color:#10b981; background:rgba(16,185,129,0.1); padding:4px 8px; border-radius:6px; border:1px solid rgba(16,185,129,0.2); }
.delegation-tag { font-size:11px; color:#cbd5e1; background:#101319; padding:4px 10px; border-radius:6px; border:1px solid #27303f; display:inline-flex; align-items:center; gap:6px; margin-bottom:10px; }

/* Metrik Kutuları */
.metric-tile { background: #101319; border: 1px solid #27303f; border-radius: 10px; padding: 14px; }
.metric-label { font-size: 10.5px; font-weight: 600; color: #8b9bb4; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px; }
.metric-val { font-size: 24px; font-weight: 800; color: #f8fafc; display:flex; align-items:baseline; gap:6px;}
.progress-track { width: 100%; height: 8px; background: #101319; border-radius: 99px; overflow: hidden; display: flex; margin-top: 14px; border: 1px solid #27303f; }
</style>""", unsafe_allow_html=True)

# Test Senaryoları
STRESS_MSGS = [
    "Yine mutfak darmadağın kalmış, her akşam ben toplamaktan gerçekten çok yoruldum artık.",
    "Hep ben hatırlatıyorum, fatura son gün gelmiş yine, tek başıma yetişemiyorum.",
    "Sürekli kedi kumu al diyorum, yine unutmuşsun. Her şeyi ben mi düşüneceğim?"
]

CRISIS_MSGS = [
    "Acil usta bulman lazım, banyoyu su bastı!",
    "Araba çalışmıyor, çekici çağırsana toplantıya geç kaldım.",
    "Kombi yine E03 hatası veriyor, donduk evde hemen yetkili servisi ara."
]

STANDARD_MSGS = [
    "Akşam gelirken marketten 2 ekmekle yoğurt alır mısın?",
    "Kedinin maması bitmiş, internetten sipariş geçer misin?",
    "Elektrik faturası gelmiş, sana zahmet akşam yatırır mısın?"
]

# Üst Bar & Versiyon Etiketi
head_col1, head_col2, head_col3 = st.columns([0.65, 5, 2.5])
with head_col1: st.image(LOGO_SVG, width=46)
with head_col2:
    st.markdown("""<div style="display:flex; flex-direction:column; justify-content:center; height:46px;">
<div style="font-size:22px; font-weight:800; letter-spacing:0.18em; color:#ffffff; line-height:1;">
NIVO <span style="font-size:11px; font-weight:700; color:#38bdf8; letter-spacing:0.05em; vertical-align:middle; margin-left:6px; background:rgba(56, 189, 248, 0.1); padding:2px 6px; border-radius:4px;">v9.0</span>
</div>
<div style="font-size:9.5px; color:#8b9bb4; letter-spacing:0.08em; text-transform:uppercase; font-weight:600; margin-top:3px;">Cognitive Balance Operating System</div>
</div>""", unsafe_allow_html=True)
with head_col3:
    st.markdown("""<div style="display:flex; justify-content:flex-end; align-items:center; height:46px; gap:8px;">
<div style="background:#171b22; border:1px solid #27303f; color:#94a3b8; padding:5px 10px; border-radius:99px; font-size:11px; font-weight:600; display:flex; align-items:center; gap:6px;"><span style="width:6px; height:6px; background:#f59e0b; border-radius:50%;"></span> Streak: 12 Gün</div>
<div style="background:#171b22; border:1px solid #27303f; color:#94a3b8; padding:5px 10px; border-radius:99px; font-size:11px; font-weight:600; display:flex; align-items:center; gap:6px;"><span style="width:6px; height:6px; background:#10b981; border-radius:50%;"></span> Core Online</div>
</div>""", unsafe_allow_html=True)

st.write("")

# ÖZENLE DENGELENMİŞ BAŞLANGIÇ VERİLERİ (Hakan: 6 Puan, Buse: 6 Puan)
if "tasks_v9" not in st.session_state:
    st.session_state.tasks_v9 = [
        # Hakan'ın Sorumlulukları (Kriz + Finans = Toplam 6 Puan)
        {"title": "Acil kombi su akıtıyor, tesisatçı bulman lazım", "due": "Bugün", "assigner": "Buse", "owner": "Hakan", "tag": "Ev Düzeni", "weight": 3, "kind": "Zihinsel", "est": "Öncelikli", "sync": True, "alert": "🚨 Kriz Uyarı: 'acil'"},
        {"title": "Araç kasko poliçelerinin yenilenmesi ve ödemesi", "due": "18 Ekim", "assigner": "Buse", "owner": "Hakan", "tag": "Finans", "weight": 3, "kind": "Zihinsel", "est": "1.5 Saat", "sync": False, "alert": ""},
        # Buse'nin Sorumlulukları (Tükenmişlik + Evcil Hayvan = Toplam 6 Puan)
        {"title": "Her akşam evi toplamaktan yoruldum, sıra sende", "due": "Yakında", "assigner": "Hakan", "owner": "Buse", "tag": "Ev Düzeni", "weight": 3, "kind": "Fiziksel", "est": "45 Dk", "sync": True, "alert": "⚠️ Pasif-agresif kalıp: 'yoruldum'"},
        {"title": "Kedinin aşı takvimi ve veteriner randevusu", "due": "Yarın", "assigner": "Hakan", "owner": "Buse", "tag": "Evcil Hayvan", "weight": 3, "kind": "Zihinsel", "est": "45 Dk", "sync": True, "alert": ""},
    ]

if "sample_v9" not in st.session_state:
    st.session_state.sample_v9 = ""

def extract_task_summary(text):
    stopwords = ["buse", "hakan", "lütfen", "rica etsem", "misin", "mısın", "musun", "müsün", "ya", "bi", "sana zahmet", "acaba", "?", "!"]
    txt = text.lower()
    for w in stopwords:
        txt = txt.replace(w, "")
    txt = " ".join(txt.split()).strip()
    if not txt: return "Rutin Görev Bildirimi"
    return txt.capitalize()[:55] + "..." if len(txt) > 55 else txt.capitalize()

col_left, col_right = st.columns([1.25, 1], gap="medium")

with col_left:
    st.markdown("""<div class="nivo-card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
<div style="font-weight:600; font-size:13.5px; color:#f8fafc;">WhatsApp Delegasyon & NLP Motoru</div>
<span style="font-size:10px; color:#64748b; font-family:monospace;">Engine v9.0 / Delegation</span>
</div>""", unsafe_allow_html=True)

    c_s1, c_s2, c_s3 = st.columns(3)
    with c_s1:
        if st.button("🚨 Tükenmişlik Örneği", use_container_width=True):
            st.session_state.sample_v9 = random.choice(STRESS_MSGS)
            st.rerun()
    with c_s2:
        if st.button("🔧 Rutin Kriz Örneği", use_container_width=True):
            st.session_state.sample_v9 = random.choice(CRISIS_MSGS)
            st.rerun()
    with c_s3:
        if st.button("🛒 Standart Örnek", use_container_width=True):
            st.session_state.sample_v9 = random.choice(STANDARD_MSGS)
            st.rerun()

    input_text = st.text_area(
        label="Mesaj",
        label_visibility="collapsed",
        value=st.session_state.sample_v9,
        placeholder="Doğal bir mesaj girin: 'Akşam gelirken marketten 2 ekmek alır mısın?'",
        height=85
    )

    c1, c2, c3 = st.columns([1.5, 1, 1.2])
    with c1:
        # Artık sadece "İleten" değil, açıkça "Gönderen"
        sender_actor = st.selectbox("Gönderen (Mesajı Yazan):", ["Hakan", "Buse"], label_visibility="collapsed")
    with c2:
        do_sync = st.checkbox("Takvime İşle", value=True)
    with c3:
        sync_btn = st.button("Senkronize Et ⚡", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if sync_btn and input_text.strip():
        txt = input_text.lower()
        title = extract_task_summary(input_text)
        
        category = "Genel"
        w = 1
        kind = "Fiziksel"
        est_time = "15 Dk"
        alert_msg = ""
        is_stressed = False

        # Tükenmişlik Analizi
        stress_words = ["yine", "hep", "yoruldum", "bıktım", "tek başıma", "sürekli", "artık", "gına", "sıkıldım", "çıldıracağım"]
        found_stress = [word for word in stress_words if word in txt]
        if found_stress:
            is_stressed = True
            w += 1 
            alert_msg = f"⚠️ Pasif-agresif kalıp: '{found_stress[0]}'"
            
        # Kriz Analizi
        urgent_words = ["acil", "hemen", "kaldım", "patlamış", "bas", "taşı", "çabuk", "bozuldu", "çalışmıyor"]
        found_urgent = [word for word in urgent_words if word in txt]
        if found_urgent:
            w += 1
            est_time = "Öncelikli"
            alert_msg = f"🚨 Kriz Uyarı: '{found_urgent[0]}'"

        # Kategori
        if any(k in txt for k in ["veteriner", "kedi", "mama", "aşı", "köpek", "kum"]):
            category, w, kind, est_time = "Evcil Hayvan", max(2, w), "Zihinsel", "45 Dk"
        elif any(k in txt for k in ["fatura", "kira", "sigorta", "ödeme", "kredi", "aidat"]):
            category, w, kind, est_time = "Finans", max(3, w), "Zihinsel", "30 Dk"
        elif any(k in txt for k in ["market", "kahve", "eczane", "ilaç", "ekmek", "su", "sipariş"]):
            category, w, kind, est_time = "Lojistik", max(2, w), "Fiziksel", "45 Dk"
        elif any(k in txt for k in ["usta", "servis", "kombi", "tamir", "çekici", "çilingir", "internet"]):
            category, w, kind, est_time = "Ev Düzeni", max(3, w), "Zihinsel", "1.5 Saat"
        elif any(k in txt for k in ["temizlik", "çöp", "bulaşık", "mutfak", "çamaşır"]):
            category, w, kind, est_time = "Ev Düzeni", max(2, w), "Fiziksel", "1 Saat"

        due = "Bugün" if found_urgent else ("Yarın" if "yarın" in txt else ("Bu Akşam" if "akşam" in txt else "Yakında"))
        
        # Akıllı Delegasyon Mantığı (Kim kime atıyor?)
        other_person = "Buse" if sender_actor == "Hakan" else "Hakan"
        
        if "ben " in txt or " hallederim" in txt or " yaparım" in txt:
            assigned_owner = sender_actor # Kişi görevi kendine alıyor
        elif is_stressed:
            assigned_owner = other_person # Stres varsa diğerine iteler
        else:
            assigned_owner = other_person # Varsayılan: Karşı tarafa rica ediyor

        st.session_state.tasks_v9.insert(0, {
            "title": title,
            "due": due,
            "assigner": sender_actor,
            "owner": assigned_owner,
            "tag": category,
            "weight": w,
            "kind": kind,
            "est": est_time,
            "sync": do_sync,
            "alert": alert_msg
        })
        st.session_state.sample_v9 = ""
        st.rerun()

    st.markdown("<div style='font-size:12.5px; font-weight:700; color:#8b9bb4; margin:16px 0 8px 2px;'>📋 AKTİF ZİHİNSEL & FİZİKSEL ENVANTER</div>", unsafe_allow_html=True)

    if st.session_state.tasks_v9:
        for idx, t in enumerate(list(st.session_state.tasks_v9)):
            col_t1, col_t2, col_t3 = st.columns([5.2, 1.1, 1.1])
            with col_t1:
                k_badge = f'<span class="badge-mental">🧠 {t["kind"]}</span>' if t["kind"] == "Zihinsel" else f'<span class="badge-phys">🛠️ {t["kind"]}</span>'
                s_badge = f'<span class="badge-sync">🗓 Sync</span>' if t.get("sync") else ""
                a_badge = f'<div class="badge-alert">{t["alert"]}</div>' if t.get("alert") else ""
                stars = "⚡" * min(t["weight"], 5)
                
                # YENİ: Gönderen -> Alan İlişkisi (Delegasyon Etiketi)
                delegation_ui = f"""<div class="delegation-tag">📤 Gönderen: <b>{t.get('assigner', 'Bilinmiyor')}</b> <span style="color:#475569;">➔</span> 👤 Sorumlu: <b style="color:#f8fafc;">{t['owner']}</b></div>"""
                
                item_html = f"""<div class="nivo-card" style="margin-bottom:8px;">
{delegation_ui}
<div style="font-weight:600; font-size:14.5px; color:#f1f5f9; margin-bottom:6px; line-height:1.4;">{t['title']}</div>
<div style="font-size:11.5px; color:#8b9bb4; margin-bottom:12px;">⏱ {t['due']} &nbsp;•&nbsp; ⏳ Tahmini Efor: {t.get("est", "N/A")}</div>
<div style="display:flex; gap:6px; align-items:center; flex-wrap: wrap;">
{k_badge} <span class="badge-category">{t['tag']}</span> <span style="font-size:11px;" title="Zorluk Derecesi">{stars}</span> {s_badge}
</div>
{a_badge}
</div>"""
                st.markdown(item_html, unsafe_allow_html=True)
            with col_t2:
                other_person = "Buse" if t["owner"] == "Hakan" else "Hakan"
                if st.button("Devret ⇄", key=f"swap_{idx}", help="Karşı tarafa aktar"):
                    st.session_state.tasks_v9[idx]["owner"] = other_person
                    st.session_state.tasks_v9[idx]["assigner"] = "Sistem/Devir"
                    st.rerun()
            with col_t3:
                if st.button("Bitir ✓", key=f"done_{idx}"):
                    st.session_state.tasks_v9.pop(idx)
                    st.rerun()
    else:
        st.info("Harika, sistem dengede. Aktif görev bulunmuyor.")

with col_right:
    
    # Hesaplamalar
    total_tasks = len(st.session_state.tasks_v9)
    h_weight = sum(t["weight"] for t in st.session_state.tasks_v9 if t["owner"] == "Hakan")
    b_weight = sum(t["weight"] for t in st.session_state.tasks_v9 if t["owner"] == "Buse")
    tot_weight = h_weight + b_weight
    h_ratio = round((h_weight / tot_weight * 100)) if tot_weight > 0 else 50
    b_ratio = 100 - h_ratio if tot_weight > 0 else 50
    
    # Yeni Metrik: İlişki Uyum Skoru (Harmony Score) - %50 dengesine ne kadar yakın?
    harmony_score = 100 - (abs(h_ratio - 50) * 2)
    harmony_color = "#10b981" if harmony_score >= 80 else ("#f59e0b" if harmony_score >= 50 else "#ef4444")

    st.markdown("<div style='font-size:12.5px; font-weight:700; color:#8b9bb4; margin:0 0 8px 2px;'>📊 GÜNLÜK KOKPİT & UYUM</div>", unsafe_allow_html=True)
    
    if harmony_score == 100:
        briefing = f"🎉 **Tebrikler, Mükemmel Denge!** Her iki taraf da tam olarak eşit zihinsel/fiziksel yük taşıyor. İletişiminiz kusursuz işliyor, bu hafta sonu birlikte güzel bir kahveyi hak ettiniz."
    elif b_ratio > 55:
        briefing = f"⚠️ Zihinsel yük %{b_ratio} oranla tehlikeli şekilde Buse'ye kaymış durumda. Hakan'ın acilen operasyonel destek verip sorumluluk devralması tavsiye edilir."
    elif h_ratio > 55:
        briefing = f"⚠️ Zihinsel yük %{h_ratio} oranla Hakan'da birikmiş durumda. Buse'nin organizasyonel konularda inisiyatif alması dengeyi sağlayacaktır."
    else:
        briefing = f"✅ Sistemde **{total_tasks} görev** var. Yük dağılımı ideal dengeye çok yakın. Operasyon sağlıklı ilerliyor."

    st.markdown(f"""<div class="nivo-card" style="border-left:3px solid {harmony_color}; background: linear-gradient(135deg, #171b22 0%, #10151c 100%); padding:18px;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
<div style="font-size:12px; font-weight:700; color:#cbd5e1;">İlişki Uyum Skoru (Harmony)</div>
<div style="font-size:20px; font-weight:800; color:{harmony_color};">%{harmony_score}</div>
</div>
<div style="font-size:12px; color:#94a3b8; line-height:1.6;">{briefing}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<div style='font-size:12.5px; font-weight:700; color:#8b9bb4; margin:20px 0 8px 2px;'>⚖️ BİLİŞSEL YÜK ANALİTİĞİ</div>", unsafe_allow_html=True)

    b_mental = sum(1 for t in st.session_state.tasks_v9 if t["owner"] == "Buse" and t["kind"] == "Zihinsel")
    h_mental = sum(1 for t in st.session_state.tasks_v9 if t["owner"] == "Hakan" and t["kind"] == "Zihinsel")

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

    st.markdown("""<div class="nivo-card" style="border-style:dashed;">
<div style="font-weight:600; font-size:11.5px; color:#cbd5e1; margin-bottom:4px;">🛡️ Sıfır Konuşma Saklama Protokolü</div>
<div style="font-size:11px; color:#64748b; line-height:1.45;">Mesajlar RAM'de işlenir ve saniyesinde JSON verisine çevrilip imha edilir. Gizlilik esastır.</div>
</div>""", unsafe_allow_html=True)
