import streamlit as st
import pandas as pd
import plotly.express as px
import time

# 1. إعدادات النظام المتقدمة
st.set_page_config(page_title="Alexandra Multi-Language OS", layout="wide", page_icon="🌐")

# 2. تصميم الواجهة الاحترافية (CSS)
st.markdown("""
    <style>
    .stApp { background: #050505; color: white; font-family: 'Cairo', sans-serif; }
    .card { background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; border: 1px solid #D4AF37; margin-bottom: 10px; }
    h1, h2 { color: #D4AF37; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. نظام الترجمة المدمج
languages = {
    "العربية": {"welcome": "مرحباً بكِ في نظام السيادة الرقمية", "map_title": "الرادار العالمي", "news": "آخر الأخبار", "media": "معرض الوسائط"},
    "English": {"welcome": "Welcome to the Digital Sovereignty System", "map_title": "Global Radar", "news": "Latest Updates", "media": "Media Gallery"},
    "Français": {"welcome": "Bienvenue dans le système de souveraineté numérique", "map_title": "Radar mondial", "news": "Dernières mises à jour", "media": "Galerie média"}
}

# اختيار اللغة من الشريط الجانبي
st.sidebar.title("🌐 Language / اللغة")
selected_lang = st.sidebar.selectbox("Select Language", list(languages.keys()))
lang_pack = languages[selected_lang]

st.title(f"🔱 {lang_pack['welcome']} 🔱")

# 4. القائمة الرئيسية
tabs = st.tabs([lang_pack['map_title'], lang_pack['news'], lang_pack['media']])

# --- تبويب الخريطة والمعلومات الدقيقة ---
with tabs[0]:
    st.header("📍 تحليل البيانات الجغرافية الدقيقة")
    # بيانات أكثر تنوعاً (اقتصاد، سكان، تقنية)
    country_data = {
        'Tunisia': {'lat': 33.8869, 'lon': 9.5375, 'GDP': '45B', 'Tech_Index': 'High', 'Info': 'بوابة الابتكار في شمال أفريقيا.'},
        'Japan': {'lat': 36.2048, 'lon': 138.2529, 'GDP': '5T', 'Tech_Index': 'Ultra', 'Info': 'مركز التطور الروبوتي العالمي.'},
        'Germany': {'lat': 51.1657, 'lon': 10.4515, 'GDP': '4T', 'Tech_Index': 'Advanced', 'Info': 'المحرك الاقتصادي لأوروبا.'}
    }
    
    df = pd.DataFrame([{'Country': k, 'lat': v['lat'], 'lon': v['lon']} for k, v in country_data.items()])
    fig = px.scatter_geo(df, lat='lat', lon='lon', hover_name='Country', projection="orthographic")
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    
    selected_country = st.selectbox("اختر بلداً لتحليل تفصيلي:", list(country_data.keys()))
    c_info = country_data[selected_country]
    st.markdown(f"""
    <div class="card">
        <h3>📊 تقرير استخباراتي: {selected_country}</h3>
        <p><b>الناتج المحلي:</b> {c_info['GDP']}</p>
        <p><b>مستوى التطور التقني:</b> {c_info['Tech_Index']}</p>
        <p><b>ملاحظات النظام:</b> {c_info['Info']}</p>
    </div>
    """, unsafe_allow_html=True)

# --- تبويب الأخبار المتنوعة ---
with tabs[1]:
    st.header("📰 رادار الأخبار العالمية")
    col1, col2 = st.columns(2)
    with col1:
        st.info("🔥 **سياسة:** تحالفات تكنولوجية جديدة تغير موازين القوى في 2026.")
    with col2:
        st.success("💰 **اقتصاد:** قفزة في أسهم شركات الذكاء الاصطناعي السيادية.")

# --- تبويب الوسائط (صور وفيديوهات) ---
with tabs[2]:
    st.header(f"🎬 {lang_pack['media']}")
    
    col_img, col_vid = st.columns(2)
    
    with col_img:
        st.subheader("🖼️ رصد بصري (Satellite)")
        # يمكنك استبدال هذه الروابط بصورك الخاصة لاحقاً
        st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=800&q=80", 
                 caption="رصد بالأقمار الصناعية لتدفق البيانات العالمي")
        
    with col_vid:
        st.subheader("🎥 تقارير فيديو")
        # رابط فيديو توضيحي (يمكنك وضع روابط YouTube هنا)
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # مثال لفيديو، استبدليه برابطك

st.sidebar.markdown("---")
st.sidebar.write(f"🔔 **إشعار:** النظام محدث لعام 2026")





