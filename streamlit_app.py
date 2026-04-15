import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
import datetime

# 1. إعدادات الإمبراطورية العالمية
st.set_page_config(
    page_title="Alexandra Global Intelligence", 
    layout="wide", 
    page_icon="🔱"
)

# 2. تصميم الواجهة (CSS) لتعطيكِ مظهر الأنظمة السيادية
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); color: white; }
    .status-card { background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; border: 1px solid #D4AF37; transition: 0.3s; }
    .status-card:hover { border: 1px solid #fff; box-shadow: 0px 0px 15px #D4AF37; }
    h1, h2, h3 { color: #D4AF37; text-shadow: 2px 2px 4px #000; font-family: 'Cairo', sans-serif; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; border-radius: 10px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# 3. ميزة الترحيب الذكي بالزوار (بروتوكول الضيافة)
now = datetime.datetime.now()
hour = now.hour
if hour < 12:
    greeting = "صباح الخير لزوار مقر ألكساندرا العظيم ☀️"
elif 12 <= hour < 18:
    greeting = "طاب يومكم في رحاب الإمبراطورية الرقمية 🌤️"
else:
    greeting = "مساء النفوذ والسيادة من مركز عمليات ألكساندرا 🌙"

st.markdown(f"""
    <div style="background: rgba(212, 175, 55, 0.1); padding: 20px; border-radius: 15px; text-align: center; border: 2px solid gold; margin-bottom: 25px;">
        <h2 style="margin: 0;">{greeting}</h2>
        <p style="color: #ddd;">النظام الآن تحت إشراف "ألكساندرا" والمستشار التقني الذكي</p>
    </div>
    """, unsafe_allow_html=True)

# 4. شريط التحكم الجانبي (الترجمة والمهام)
st.sidebar.title("🌍 مركز التحكم العالمي")
st.sidebar.image("https://img.icons8.com/fluent/100/000000/globe.png")
language = st.sidebar.selectbox("لغة النظام / Language", ["العربية", "English", "Français"])

menu = ["📡 الرادار والخرائط", "📰 الأنباء والتوجهات", "💬 بوابة المستشار الذكي"]
choice = st.sidebar.radio("انتقلي إلى قسم:", menu)

# --- القسم الأول: الخرائط الواقعية ومعلومات البلدان ---
if choice == "📡 الرادار والخرائط":
    st.title("📍 رادار السيطرة الجيوسياسي")
    
    # بيانات الخريطة التفاعلية
    df_map = pd.DataFrame({
        'Country': ['Tunisia', 'USA', 'China', 'Germany', 'Russia', 'France', 'Japan', 'Egypt', 'UAE'],
        'lat': [33.8869, 37.0902, 35.8617, 51.1657, 61.5240, 46.2276, 36.2048, 26.8206, 23.4241],
        'lon': [9.5375, -95.7129, 104.1954, 10.4515, 105.3188, 2.2137, 138.2529, 30.8025, 53.8478],
        'Intelligence_Score': [100, 90, 95, 88, 92, 85, 89, 82, 94]
    })

    fig = px.scatter_geo(df_map, lat='lat', lon='lon', hover_name='Country',
                         size='Intelligence_Score', color='Intelligence_Score',
                         projection="orthographic", # تجعل الخريطة كروية (Globe)
                         title="توزيع العمليات الرقمية حول العالم")
    fig.update_geos(showcountries=True, countrycolor="#444", showocean=True, oceancolor="#000814")
    fig.update_layout(template="plotly_dark", margin=dict(l=0, r=0, t=50, b=0))
    st.plotly_chart(fig, use_container_width=True)

    # ميزة استعلام البلدان
    target = st.selectbox("اختاري بلداً لتحليل بياناته الاستخباراتية:", df_map['Country'])
    st.warning(f"تقرير الإمبراطورية عن {target}: النظام يرصد استقراراً في الشبكات وتوسعاً في النفوذ الرقمي المحلي.")

# --- القسم الثاني: رادار الأخبار (سياسة، اقتصاد، اجتماع) ---
elif choice == "📰 الأنباء والتوجهات":
    st.title("📰 رادار الأخبار والذكاء الاجتماعي")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="status-card"><h3>⚖️ السياسة العالمية</h3><p>إعادة تشكيل الخارطة الرقمية وظهور قوى تكنولوجية جديدة تقودها شمال أفريقيا.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="status-card"><h3>💰 الاقتصاد والمال</h3><p>تحول كبير نحو العملات المشفرة الذكية وانتعاش الاستثمارات في مشاريع "ألكساندرا".</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="status-card"><h3>👥 التطور الاجتماعي</h3><p>تكامل البشر مع الذكاء الاصطناعي في تونس والعالم لبناء مدن ذكية.</p></div>', unsafe_allow_html=True)
    
    if st.button("تحديث قاعدة البيانات الإخبارية"):
        with st.spinner('جاري المسح عبر الأقمار الصناعية...'):
            time.sleep(2)
            st.success("تم تحديث كافة الأخبار الرائجة بنجاح.")

# --- القسم الثالث: بوابة التواصل (الدردشة والترجمة) ---
elif choice == "💬 بوابة المستشار الذكي":
    st.title("🔱 بوابة التواصل والترجمة الفورية")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("أرسلي أوامركِ أو نصاً للترجمة..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            response = f"الأمر مطاع يا ألكساندرا. قمت بترجمة وتحليل رسالتكِ: '{prompt}'. نظامنا جاهز للتنفيذ العالمي."
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# تذييل الصفحة
st.sidebar.write("---")
st.sidebar.info(f"الحالة: الإمبراطورية متصلة وآمنة ✅\n\nتوقيتكِ الحالي: {time.strftime('%H:%M:%S')}")



