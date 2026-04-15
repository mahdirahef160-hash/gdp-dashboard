import streamlit as st
import pandas as pd
import plotly.express as px
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Alexandra Global OS", layout="wide", page_icon="🔱")

# 2. تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .stApp { background: #000000; color: white; }
    .card { background: rgba(212, 175, 55, 0.1); padding: 20px; border-radius: 15px; border: 1px solid #D4AF37; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { background-color: rgba(255,255,255,0.05); border-radius: 10px; padding: 10px 20px; color: gold; }
    </style>
    """, unsafe_allow_html=True)

# 3. محرك الترجمة الذكي
languages = {
    "العربية": {
        "title": "مرحباً بكِ في عصر السيادة الرقمية",
        "tab1": "📍 الرادار العالمي",
        "tab2": "🖼️ معرض الوسائط",
        "tab3": "💬 التواصل والمستشار",
        "country_label": "اختر بلداً لتحليل دقيق:",
        "gdp": "الناتج المحلي الإجمالي:",
        "tech": "مستوى التطور الرقمي:",
        "news": "آخر التقارير الاستخباراتية"
    },
    "English": {
        "title": "Welcome to the Era of Digital Sovereignty",
        "tab1": "📍 Global Radar",
        "tab2": "🖼️ Media Gallery",
        "tab3": "💬 Intelligence Chat",
        "country_label": "Choose a country for analysis:",
        "gdp": "Gross Domestic Product (GDP):",
        "tech": "Digital Advancement Level:",
        "news": "Latest Intel Reports"
    },
    "Français": {
        "title": "Bienvenue dans l'ère de la souveraineté numérique",
        "tab1": "📍 Radar Mondial",
        "tab2": "🖼️ Galerie Médias",
        "tab3": "💬 Chat d'Intelligence",
        "country_label": "Choisissez un pays pour l'analyse:",
        "gdp": "Produit Intérieur Brut (PIB):",
        "tech": "Niveau de Progrès Numérique:",
        "news": "Derniers Rapports"
    }
}

# اختيار اللغة من الشريط الجانبي
st.sidebar.title("🌐 Language Selection")
selected_lang = st.sidebar.selectbox("اختر لغة النظام / Select Language", list(languages.keys()))
L = languages[selected_lang]

st.title(f"🔱 {L['title']} 🔱")

# 4. التبويبات الرئيسية (Tabs)
tabs = st.tabs([L['tab1'], L['tab2'], L['tab3']])

# --- القسم الأول: الرادار والمعلومات الدقيقة ---
with tabs[0]:
    st.header(L['tab1'])
    
    # بيانات دقيقة
    countries = {
        'Tunisia': {'gdp': '46.66 Billion USD', 'tech': 'Excellent (Hub of Africa)', 'lat': 33.8869, 'lon': 9.5375, 'img': 'https://images.unsplash.com/photo-1590059235ef9-548455e997f1?q=80&w=1000'},
        'Japan': {'gdp': '4.93 Trillion USD', 'tech': 'Ultra Advanced', 'lat': 36.2048, 'lon': 138.2529, 'img': 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=1000'},
        'Germany': {'gdp': '4.22 Trillion USD', 'tech': 'High Industry 4.0', 'lat': 51.1657, 'lon': 10.4515, 'img': 'https://images.unsplash.com/photo-1467269204594-9661b134dd2b?q=80&w=1000'},
        'USA': {'gdp': '23.32 Trillion USD', 'tech': 'Global Tech Leader', 'lat': 37.0902, 'lon': -95.7129, 'img': 'https://images.unsplash.com/photo-1501594907352-04cda38ebc29?q=80&w=1000'}
    }
    
    # عرض الخريطة
    df = pd.DataFrame([{'Country': k, 'lat': v['lat'], 'lon': v['lon']} for k, v in countries.items()])
    fig = px.scatter_geo(df, lat='lat', lon='lon', hover_name='Country', projection="orthographic")
    fig.update_layout(template="plotly_dark", margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig, use_container_width=True)

    # اختيار البلد وعرض صورته ومعلوماته
    c_choice = st.selectbox(L['country_label'], list(countries.keys()))
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(countries[c_choice]['img'], caption=f"View of {c_choice}", use_container_width=True)
    
    with col2:
        st.markdown(f"""
        <div class="card">
            <h3>📊 {L['news']}: {c_choice}</h3>
            <p><b>{L['gdp']}</b> {countries[c_choice]['gdp']}</p>
            <p><b>{L['tech']}</b> {countries[c_choice]['tech']}</p>
            <hr>
            <p>نظام ألكساندرا يؤكد استمرارية السيطرة الرقمية في هذه المنطقة.</p>
        </div>
        """, unsafe_allow_html=True)

# --- القسم الثاني: معرض الوسائط (فيديوهات وصور) ---
with tabs[1]:
    st.header(L['tab2'])
    st.write("تقارير مرئية من جميع أنحاء الكوكب:")
    
    v_col1, v_col2 = st.columns(2)
    with v_col1:
        st.subheader("📺 البث الاستخباراتي")
        # فيديو عن التكنولوجيا المستقبلية
        st.video("https://www.youtube.com/watch?v=f39f7-6K6N0") 
        
    with v_col2:
        st.subheader("🖼️ صور الأقمار الصناعية")
        st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1000", caption="شبكة البيانات العالمية")

# --- القسم الثالث: المستشار الذكي ---
with tabs[2]:
    st.header(L['tab3'])
    chat_input = st.chat_input("أدخلي أوامركِ هنا...")
    if chat_input:
        st.chat_message("user").write(chat_input)
        st.chat_message("assistant").write(f"الأمر مطاع يا إمبراطورة. تم تفعيل البروتوكول الخاص بـ: {chat_input}")

st.sidebar.markdown("---")
st.sidebar.success(f"Language: {selected_lang}")
    
