import streamlit as st
import random
import json
import os

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
div.stButton > button { background-color: #242c38 !important; color: #f8fafc !important; border: 1px solid #384558 !important; border-radius: 10px !important; font-weight: 600 !important; font-size: 13px !important; padding: 0.5rem 1rem !important; transition: all 0.2s; }
div.stButton > button:hover { background-color: #2d3746 !important; border-color: #4b5c75 !important; color: #ffffff !important; }

/* Dengeleme Butonu Nabız (Pulse) Efekti */
@keyframes pulseGlow {
    0% { box-shadow: 0 0 0 0 rgba(56, 189, 248, 0.5); transform: scale(1); }
    50% { box-shadow: 0 0 20px 5px rgba(56, 189, 248, 0.2); transform: scale(1.02); }
    100% { box-shadow: 0 0 0 0 rgba(56, 189, 248, 0); transform: scale(1); }
}
.ai-balance-btn > button { 
    background: linear-gradient(135deg, #0284c7 0%, #3b82f6 100%) !important; 
    border: none !important; 
    color: white !important;
    animation: pulseGlow 2s infinite;
}

/* Rozetler */
.badge-category { background-color: #101319; border: 1px solid #27303f; color: #94a3b8; border-radius: 6px; padding: 4px 8px; font-size: 10.5px; font-weight: 600; white-space:nowrap; }
.badge-mental { background-color: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.25); color: #38bdf8; border-radius: 6px; padding: 4px 8px; font-size: 10.5px; font-weight: 600; white-space:nowrap;}
.badge-phys { background-color: rgba(148, 163, 184, 0.1); border: 1px solid rgba(148, 163, 184, 0.2); color: #cbd5e1; border-radius: 6px; padding: 4px 8px; font-size: 10.5px; font-weight: 600; white-space:nowrap;}
.badge-alert { background-color: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); color: #f87171; border-radius: 6px; padding: 4px 8px; font-size: 10.5px; font-weight: 700; display: inline-block; margin-top:8px;}
.delegation-tag { font-size:11px; color:#cbd5e1; background:#101319; padding:5px 10px; border-radius:6px; border:1px solid #27303f; display:inline-flex; align-items:center; gap:6px; margin-bottom:12px; }
.task-title { font-weight:600; font-size:14.5px; color:#f1f5f9; margin-bottom:8px; line-height:1.5; word-wrap: break-word; white-space: pre-wrap; }

/* Sekmeler */
.stTabs [data-baseweb="tab-list"] { gap: 8px; background-color: transparent; }
.stTabs [data-baseweb="tab"] { background-color: #171b22; border: 1px solid #27303f; border-radius: 8px; padding: 8px 16px; color: #94a3b8; font-weight: 600; font-size:13.5px; }
.stTabs [aria-selected="true"] { background-color: #1e293b !important; color: #f8fafc !important; border-color: #38bdf8 !important; }

/* Metrik Kutuları */
.metric-tile { background: #101319; border: 1px solid #27303f; border-radius: 10px; padding: 14px; }
.metric-label { font-size: 10px; font-weight: 700; color: #8b9bb4; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px; }
.metric-val { font-size: 22px; font-weight: 800; color: #f8fafc; display:flex; align-items:baseline; gap:6px;}
.progress-track { width: 100%; height: 8px; background: #101319; border-radius: 99px; overflow: hidden; display: flex; margin-top: 14px; border: 1px solid #27303f; }
</style>""", unsafe_allow_html=True)

# SİMÜLASYON MESAJ HAVUZU
STRESS_MSGS = [
    "Yine mutfak darmadağın kalmış, her akşam ben toplamaktan gerçekten çok yoruldum artık.",
    "Hep ben hatırlatıyorum, fatura son gün gelmiş yine, tek başıma yetişemiyorum.",
    "Sürekli marketi ben düşünüyorum, yine unutmuşsun. Her şeyi ben mi düşüneceğim?",
    "Çamaşırları asmayı yine unutmuşsun, makinede kokmuş hep bıktım ya.",
    "Bıktım artık her şeyi arkandan toplamaktan, biraz inisiyatif al."
]
CRISIS_MSGS = [
    "Acil usta bulman lazım, banyoyu su bastı!",
    "Kombi yine E03 hatası veriyor, donduk evde hemen yetkili servisi ara.",
    "Kedinin midesi bozuldu çok kusuyor, acil veterineri ara randevu al.",
    "Araba çalışmıyor, çekici çağırsana acil geç kaldım.",
    "Elektrikler gitti sunumum var, acil müşteri hizmetlerini ara."
]
STANDARD_MSGS = [
    "Akşam gelirken marketten 2 ekmekle yoğurt alır mısın?",
    "Elektrik faturası gelmiş, sana zahmet akşam yatırır mısın?",
    "Haftasonu annemlere gideceğiz, planını ona göre yap lütfen.",
    "Kedinin maması bitmiş, internetten sipariş geçer misin?",
    "Akşama makarna yapacağım, gelirken krema ve mantar alır mısın?"
]

# v17.0 İÇİN YEPYENİ VERİTABANI DOSYASI
DATA_FILE = "nivo_core_v17.json"

DEFAULT_TASKS = [
    {"id": 1, "title": "Kedinin aşı takvimi ve veteriner randevusu", "due": "Bugün", "assigner": "Hakan", "owner": "Buse", "tag": "Evcil Hayvan", "weight": 3, "kind": "Zihinsel", "est": "45 Dk", "sync": True, "alert": ""},
    {"id": 2, "title": "Bütün evin detaylı toparlanması ve temizliği", "due": "Bugün", "assigner": "Hakan", "owner": "Buse", "tag": "Ev Düzeni", "weight": 2, "kind": "Fiziksel", "est": "2 Saat", "sync": False, "alert": "⚠️ Pasif-agresif kalıp: 'yoruldum'"},
    {"id": 3, "title": "Kira ve elektrik faturasının son gün ödemesi", "due": "Yarın", "assigner": "Hakan", "owner": "Buse", "tag": "Finans", "weight": 3, "kind": "Zihinsel", "est": "30 Dk", "sync": True, "alert": ""},
    {"id": 4, "title": "Haftalık mutfak alışverişi ve yemek planlaması", "due": "Bu Akşam", "assigner": "Hakan", "owner": "Buse", "tag": "Lojistik", "weight": 2, "kind": "Zihinsel", "est": "1 Saat", "sync": True, "alert": ""},
    {"id": 5, "title": "Instagram reels post planlaması", "due": "Yarın", "assigner": "Hakan", "owner": "Buse", "tag": "Sosyal Medya", "weight": 3, "kind": "Zihinsel", "est": "1.5 Saat", "sync": True, "alert": ""},
    {"id": 6, "title": "Bozuk kombi için acil yetkili servis aranması", "due": "Bugün", "assigner": "Hakan", "owner": "Buse", "tag": "Ev Düzeni", "weight": 3, "kind": "Zihinsel", "est": "Öncelikli", "sync": True, "alert": "🚨 Kriz Uyarı: 'acil'"},
    {"id": 7, "title": "Çamaşırların yıkanıp akşamında ütülenmesi", "due": "Yarın", "assigner": "Hakan", "owner": "Buse", "tag": "Ev Düzeni", "weight": 2, "kind": "Fiziksel", "est": "1 Saat", "sync": False, "alert": ""},
    {"id": 8, "title": "Misafirler için hafta sonu yemeği organizasyonu", "due": "Hafta Sonu", "assigner": "Hakan", "owner": "Buse", "tag": "Genel", "weight": 3, "kind": "Zihinsel", "est": "1 Saat", "sync": True, "alert": ""},
    {"id": 9, "title": "Eczaneden biten günlük ilaçların tedariği", "due": "Bu Akşam", "assigner": "Hakan", "owner": "Buse", "tag": "Lojistik", "weight": 1, "kind": "Fiziksel", "est": "15 Dk", "sync": False, "alert": ""},
    {"id": 10, "title": "YouTube senaryo taslağının bitirilmesi", "due": "Yakında", "assigner": "Hakan", "owner": "Buse", "tag": "Prodüksiyon", "weight": 3, "kind": "Zihinsel", "est": "2 Saat", "sync": True, "alert": ""},
    
    {"id": 11, "title": "Oyun dosyalarının Steam'den doğrulanıp güncellenmesi", "due": "Bugün", "assigner": "Buse", "owner": "Hakan", "tag": "Ev Düzeni", "weight": 1, "kind": "Fiziksel", "est": "15 Dk", "sync": False, "alert": ""},
    {"id": 12, "title": "Ekipmanların kargoya teslim edilmesi", "due": "Yarın", "assigner": "Buse", "owner": "Hakan", "tag": "Lojistik", "weight": 2, "kind": "Fiziksel", "est": "45 Dk", "sync": True, "alert": ""},
]

def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return DEFAULT_TASKS.copy()
    else:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_TASKS, f, ensure_ascii=False, indent=4)
        return DEFAULT_TASKS.copy()

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

# YEPYENİ STATE İSİMLERİ İLE ESKİ HAFIZAYI SIFIRLADIK
if "tasks_v17" not in st.session_state: st.session_state.tasks_v17 = load_tasks()
if "sample_v17" not in st.session_state: st.session_state.sample_v17 = ""
if "ai_msg_v17" not in st.session_state: st.session_state.ai_msg_v17 = None

# ÜST BAR
head_col1, head_col2, head_col3 = st.columns([0.65, 5, 2.5])
with head_col1: st.image(LOGO_SVG, width=46)
with head_col2:
    st.markdown("""<div style="display:flex; flex-direction:column; justify-content:center; height:46px;">
<div style="font-size:22px; font-weight:800; letter-spacing:0.18em; color:#ffffff; line-height:1;">
NIVO <span style="font-size:11px; font-weight:700; color:#10b981; letter-spacing:0.05em; vertical-align:middle; margin-left:6px; background:rgba(16, 185, 129, 0.1); padding:2px 6px; border-radius:4px;">v17.0 LIVE</span>
</div>
<div style="font-size:9.5px; color:#8b9bb4; letter-spacing:0.08em; text-transform:uppercase; font-weight:600; margin-top:3px;">Cognitive Balance Operating System</div>
</div>""", unsafe_allow_html=True)
with head_col3:
    st.markdown("""<div style="display:flex; justify-content:flex-end; align-items:center; height:46px; gap:8px;">
<div style="background:#171b22; border:1px solid #27303f; color:#94a3b8; padding:5px 10px; border-radius:99px; font-size:11px; font-weight:600; display:flex; align-items:center; gap:6px;"><span style="width:6px; height:6px; background:#f59e0b; border-radius:50%;"></span> Streak: 12 Gün</div>
<div style="background:#171b22; border:1px solid #27303f; color:#94a3b8; padding:5px 10px; border-radius:99px; font-size:11px; font-weight:600; display:flex; align-items:center; gap:6px;"><span style="width:6px; height:6px; background:#10b981; border-radius:50%;"></span> DB Online</div>
</div>""", unsafe_allow_html=True)

st.write("")

def extract_task_summary(text):
    stopwords = ["buse", "hakan", "lütfen", "rica etsem", "misin", "mısın", "musun", "müsün", "ya", "bi", "sana zahmet", "acaba", "?", "!"]
    txt = text.lower()
    for w in stopwords: txt = txt.replace(w, "")
    txt = " ".join(txt.split()).strip()
    return txt.capitalize() if txt else "Rutin Görev Bildirimi"

tab1, tab2 = st.tabs(["🎛️ Ana Kokpit", "📊 Derin Analitik & Röntgen"])

with tab1:
    col_left, col_right = st.columns([1.25, 1], gap="medium")

    with col_left:
        st.markdown("""<div class="nivo-card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
<div style="font-weight:600; font-size:13.5px; color:#f8fafc;">WhatsApp Delegasyon & NLP Motoru</div>
<span style="font-size:10px; color:#10b981; font-family:monospace;">Disk Storage Active</span>
</div>""", unsafe_allow_html=True)

        c_s1, c_s2, c_s3 = st.columns(3)
        with c_s1:
            if st.button("🚨 Tükenmişlik Örneği", use_container_width=True):
                st.session_state.sample_v17 = random.choice(STRESS_MSGS)
                st.rerun()
        with c_s2:
            if st.button("🔧 Rutin Kriz Örneği", use_container_width=True):
                st.session_state.sample_v17 = random.choice(CRISIS_MSGS)
                st.rerun()
        with c_s3:
            if st.button("🛒 Standart Örnek", use_container_width=True):
                st.session_state.sample_v17 = random.choice(STANDARD_MSGS)
                st.rerun()

        input_text = st.text_area(label="Mesaj", label_visibility="collapsed", value=st.session_state.sample_v17, placeholder="Doğal bir mesaj girin...", height=85)

        c1, c2, c3 = st.columns([1.5, 1, 1.2])
        with c1:
            sender_actor = st.selectbox("Gönderen (Mesajı Yazan):", ["Hakan", "Buse"], label_visibility="collapsed")
        with c2:
            do_sync = st.checkbox("Takvime İşle", value=True)
        with c3:
            sync_btn = st.button("Senkronize Et ⚡", use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

        if sync_btn and input_text.strip():
            txt = input_text.lower()
            title = extract_task_summary(input_text)
            
            category, w, kind, est_time, alert_msg = "Genel", 1, "Fiziksel", "15 Dk", ""
            is_stressed = False

            stress_words = ["yine", "hep", "yoruldum", "bıktım", "tek başıma", "sürekli", "artık", "gına", "sıkıldım", "çıldıracağım"]
            found_stress = [word for word in stress_words if word in txt]
            if found_stress:
                is_stressed = True
                w += 2 
                alert_msg = f"⚠️ Pasif-agresif kalıp: '{found_stress[0]}'"
                
            urgent_words = ["acil", "hemen", "kaldım", "patlamış", "bas", "taşı", "çabuk", "bozuldu", "çalışmıyor"]
            found_urgent = [word for word in urgent_words if word in txt]
            if found_urgent:
                w += 1
                est_time = "Öncelikli"
                alert_msg = f"🚨 Kriz Uyarı: '{found_urgent[0]}'"

            if any(k in txt for k in ["veteriner", "kedi", "mama", "aşı", "köpek", "kum"]): category, w, kind, est_time = "Evcil Hayvan", max(2, w), "Zihinsel", "45 Dk"
            elif any(k in txt for k in ["fatura", "kira", "sigorta", "ödeme", "kredi", "aidat"]): category, w, kind, est_time = "Finans", max(3, w), "Zihinsel", "30 Dk"
            elif any(k in txt for k in ["market", "kahve", "eczane", "ilaç", "ekmek", "su", "sipariş"]): category, w, kind, est_time = "Lojistik", max(2, w), "Fiziksel", "45 Dk"
            elif any(k in txt for k in ["usta", "servis", "kombi", "tamir", "çekici", "çilingir", "internet"]): category, w, kind, est_time = "Ev Düzeni", max(3, w), "Zihinsel", "1.5 Saat"
            elif any(k in txt for k in ["temizlik", "çöp", "bulaşık", "mutfak", "çamaşır"]): category, w, kind, est_time = "Ev Düzeni", max(2, w), "Fiziksel", "1 Saat"

            due = "Bugün" if found_urgent else ("Yarın" if "yarın" in txt else ("Bu Akşam" if "akşam" in txt else "Yakında"))
            other_person = "Buse" if sender_actor == "Hakan" else "Hakan"
            
            assigned_owner = sender_actor if any(x in txt for x in ["ben ", " hallederim", " yaparım"]) else (other_person if is_stressed else other_person)

            st.session_state.tasks_v17.insert(0, {
                "id": random.randint(10000, 99999), "title": title, "due": due, "assigner": sender_actor,
                "owner": assigned_owner, "tag": category, "weight": w, "kind": kind, "est": est_time,
                "sync": do_sync, "alert": alert_msg
            })
            save_tasks(st.session_state.tasks_v17)
            st.session_state.sample_v17 = ""
            st.session_state.ai_msg_v17 = None
            st.rerun()

        if st.session_state.ai_msg_v17:
            st.success(st.session_state.ai_msg_v17)

        st.markdown(f"<div style='font-size:12.5px; font-weight:700; color:#8b9bb4; margin:16px 0 8px 2px;'>📋 AKTİF ENVANTER ({len(st.session_state.tasks_v17)} GÖREV)</div>", unsafe_allow_html=True)

        if st.session_state.tasks_v17:
            for idx, t in enumerate(list(st.session_state.tasks_v17)):
                col_t1, col_t2, col_t3 = st.columns([5.2, 1.2, 1.2])
                with col_t1:
                    k_badge = f'<span class="badge-mental">🧠 {t["kind"]}</span>' if t["kind"] == "Zihinsel" else f'<span class="badge-phys">🛠️ {t["kind"]}</span>'
                    a_badge = f'<div class="badge-alert">{t["alert"]}</div>' if t.get("alert") else ""
                    stars = "⚡" * min(t["weight"], 5)
                    assigner_display = "🤖 NIVO AI" if t.get('assigner') == "NIVO AI" else t.get('assigner', 'Bilinmiyor')
                    assigner_color = "#38bdf8" if assigner_display == "🤖 NIVO AI" else "#cbd5e1"
                    
                    item_html = f"""<div class="nivo-card" style="margin-bottom:8px;">
<div class="delegation-tag">📤 Gönderen: <b style="color:{assigner_color};">{assigner_display}</b> <span style="color:#475569;">➔</span> 👤 Sorumlu: <b style="color:#f8fafc;">{t['owner']}</b></div>
<div class="task-title">{t['title']}</div>
<div style="font-size:11.5px; color:#8b9bb4; margin-bottom:12px;">⏱ {t['due']} &nbsp;•&nbsp; ⏳ Tahmini Efor: {t.get("est", "N/A")}</div>
<div style="display:flex; gap:6px; align-items:center; flex-wrap: wrap;">
{k_badge} <span class="badge-category">{t['tag']}</span> <span style="font-size:11px;" title="Zorluk Derecesi">{stars}</span>
</div>
{a_badge}
</div>"""
                    st.markdown(item_html, unsafe_allow_html=True)
                with col_t2:
                    other_person = "Buse" if t["owner"] == "Hakan" else "Hakan"
                    if st.button("Devret ⇄", key=f"swap_{t['id']}", help="Karşı tarafa aktar"):
                        st.session_state.tasks_v17[idx]["owner"] = other_person
                        st.session_state.tasks_v17[idx]["assigner"] = "Devredildi"
                        st.session_state.ai_msg_v17 = None
                        save_tasks(st.session_state.tasks_v17)
                        st.rerun()
                with col_t3:
                    if st.button("Bitir ✓", key=f"done_{t['id']}"):
                        completed_task = st.session_state.tasks_v17.pop(idx)
                        st.session_state.ai_msg_v17 = None
                        save_tasks(st.session_state.tasks_v17)
                        if completed_task["weight"] >= 3:
                            other_p = "Hakan" if completed_task["owner"] == "Buse" else "Buse"
                            st.toast(f"💌 Harika! {completed_task['owner']} ağır bir Zihinsel Yükü temizledi. NIVO: {other_p}, ona teşekkür etmek ister misin?", icon="🎉")
                        st.rerun()
        else:
            st.info("Harika, sistem dengede. Aktif görev bulunmuyor.")
            
        if st.button("🗑️ Veritabanını Sıfırla"):
            st.session_state.tasks_v17 = DEFAULT_TASKS.copy()
            save_tasks(st.session_state.tasks_v17)
            st.rerun()

    with col_right:
        total_tasks = len(st.session_state.tasks_v17)
        h_weight = sum(t["weight"] for t in st.session_state.tasks_v17 if t["owner"] == "Hakan")
        b_weight = sum(t["weight"] for t in st.session_state.tasks_v17 if t["owner"] == "Buse")
        tot_weight = h_weight + b_weight
        h_ratio = round((h_weight / tot_weight * 100)) if tot_weight > 0 else 50
        b_ratio = 100 - h_ratio if tot_weight > 0 else 50
        
        harmony_score = 100 - (abs(h_ratio - 50) * 2)
        if harmony_score < 0: harmony_score = 0
        harmony_color = "#10b981" if harmony_score >= 80 else ("#f59e0b" if harmony_score >= 50 else "#ef4444")

        st.markdown("<div style='font-size:12.5px; font-weight:700; color:#8b9bb4; margin:0 0 8px 2px;'>📊 GÜNLÜK KOKPİT & TAHMİN</div>", unsafe_allow_html=True)
        
        today_tasks = sum(1 for t in st.session_state.tasks_v17 if t["due"] == "Bugün")
        bottleneck_msg = f"⏳ **Kritik Darboğaz Uyarısı:** Bugün teslim edilecek {today_tasks} acil iş birikti. Akşam saatlerinde stres seviyesi zirve yapabilir." if today_tasks >= 3 else ("⏳ **Darboğaz Uyarısı:** Bugün teslim edilecek görevler birikiyor." if today_tasks > 1 else "✅ Yakın vadede zamanlama darboğazı görünmüyor.")

        if harmony_score == 100: briefing = f"🎉 **Mükemmel Denge!** İletişiminiz kusursuz, hiçbir müdahaleye gerek yok."
        elif b_ratio > 55: briefing = f"🚨 Zihinsel ve fiziksel yük %{b_ratio} oranla tehlikeli şekilde Buse'ye yığılmış durumda. Hakan'ın acilen müdahale etmesi gerekiyor."
        else: briefing = f"🚨 Zihinsel ve fiziksel yük %{h_ratio} oranla tehlikeli şekilde Hakan'a yığılmış durumda. Buse'nin acilen müdahale etmesi gerekiyor."

        st.markdown(f"""<div class="nivo-card" style="border-left:4px solid {harmony_color}; background: linear-gradient(135deg, #171b22 0%, #10151c 100%); padding:16px;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
<div style="font-size:12px; font-weight:700; color:#cbd5e1;">İlişki Uyum Skoru (Harmony)</div>
<div style="font-size:24px; font-weight:800; color:{harmony_color};">%{harmony_score}</div>
</div>
<div style="font-size:12.5px; color:#94a3b8; line-height:1.5; margin-bottom:10px;">{briefing}</div>
<div style="font-size:11.5px; color:#ef4444; background:rgba(239, 68, 68, 0.08); padding:8px; border-radius:6px; border: 1px solid rgba(239, 68, 68, 0.2);">{bottleneck_msg}</div>
</div>""", unsafe_allow_html=True)

        if harmony_score < 70 and len(st.session_state.tasks_v17) > 1:
            st.markdown("<div class='ai-balance-btn'>", unsafe_allow_html=True)
            if st.button("🤖 NIVO AI: Acil Yük Dengele", use_container_width=True):
                overloaded = "Hakan" if h_weight > b_weight else "Buse"
                underloaded = "Buse" if overloaded == "Hakan" else "Hakan"
                target_shift = abs(h_weight - b_weight) / 2
                
                over_tasks = [t for t in st.session_state.tasks_v17 if t["owner"] == overloaded]
                over_tasks.sort(key=lambda x: x["weight"], reverse=True) 
                
                shifted_weight = 0
                moved_count = 0
                for t in over_tasks:
                    if shifted_weight + t["weight"] <= target_shift + 1:
                        for main_t in st.session_state.tasks_v17:
                            if main_t["id"] == t["id"]:
                                main_t["owner"] = underloaded
                                main_t["assigner"] = "NIVO AI"
                                shifted_weight += main_t["weight"]
                                moved_count += 1
                                break
                    if shifted_weight >= target_shift: break
                
                if moved_count > 0: 
                    st.session_state.ai_msg_v17 = f"✅ NIVO AI, eşitsizliği gidermek için {moved_count} ağır görevi {overloaded}'dan alıp {underloaded}'a devretti! Harmony skoru yükseldi."
                    save_tasks(st.session_state.tasks_v17)
                else: 
                    st.session_state.ai_msg_v17 = "Görev ağırlıkları bölüşüme izin vermiyor, kartlar üzerinden manuel devretmeniz önerilir."
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div style='font-size:12.5px; font-weight:700; color:#8b9bb4; margin:20px 0 8px 2px;'>⚖️ BİLİŞSEL EFOR İNDEKSİ</div>", unsafe_allow_html=True)

        b_mental = sum(1 for t in st.session_state.tasks_v17 if t["owner"] == "Buse" and t["kind"] == "Zihinsel")
        h_mental = sum(1 for t in st.session_state.tasks_v17 if t["owner"] == "Hakan" and t["kind"] == "Zihinsel")

        st.markdown(f"""<div class="nivo-card">
<div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
<div class="metric-tile">
<div class="metric-label">Hakan Toplam Yük</div>
<div class="metric-val">%{h_ratio}</div>
<div style="font-size:10px; color:#38bdf8; margin-top:6px;">🧠 {h_mental} Zihinsel İş</div>
</div>
<div class="metric-tile">
<div class="metric-label">Buse Toplam Yük</div>
<div class="metric-val">%{b_ratio}</div>
<div style="font-size:10px; color:#38bdf8; margin-top:6px;">🧠 {b_mental} Zihinsel İş</div>
</div>
</div>
<div class="progress-track">
<div style="width:{h_ratio}%; background:#38bdf8; transition:width 0.4s ease;"></div>
<div style="width:{b_ratio}%; background:#334155; transition:width 0.4s ease;"></div>
</div>
</div>""", unsafe_allow_html=True)

with tab2:
    st.markdown("<div style='font-size:15px; font-weight:700; color:#f8fafc; margin:10px 0 20px 0;'>🔍 Kategori Bazlı Emek Analizi</div>", unsafe_allow_html=True)
    
    cats = {}
    for t in st.session_state.tasks_v17:
        c = t["tag"]
        if c not in cats: cats[c] = {"Hakan": 0, "Buse": 0}
        cats[c][t["owner"]] += t["weight"]
        
    if not cats:
        st.info("Henüz analiz edilecek veri yok.")
    else:
        c1, c2 = st.columns(2)
        items = list(cats.items())
        for i, (cat_name, data) in enumerate(items):
            tot = data["Hakan"] + data["Buse"]
            h_pct = int((data["Hakan"] / tot) * 100) if tot > 0 else 0
            b_pct = 100 - h_pct if tot > 0 else 0
            
            html = f"""<div class="nivo-card" style="padding:14px;">
            <div style="font-size:13px; font-weight:700; color:#cbd5e1; margin-bottom:8px;">📌 {cat_name}</div>
            <div style="display:flex; justify-content:space-between; font-size:11px; color:#94a3b8; margin-bottom:4px;">
                <span>Hakan (%{h_pct})</span><span>Buse (%{b_pct})</span>
            </div>
            <div class="progress-track" style="margin-top:0; height:6px;">
                <div style="width:{h_pct}%; background:#38bdf8;"></div>
                <div style="width:{b_pct}%; background:#64748b;"></div>
            </div>
            </div>"""
            if i % 2 == 0:
                with c1: st.markdown(html, unsafe_allow_html=True)
            else:
                with c2: st.markdown(html, unsafe_allow_html=True)
