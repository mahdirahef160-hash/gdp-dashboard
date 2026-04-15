import streamlit as st

# إعدادات الصفحة الفخمة
st.set_page_config(page_title="Alexandra Empire", page_icon="🔱", layout="wide")

# تصميم الواجهة باستخدام CSS لجعلها تبدو كالمحترفين
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
    }
    h1 {
        text-align: center;
        color: #00d4ff;
        text-shadow: 2px 2px 5px #000;
    }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.title("🔱 المقر السري للإمبراطورة ألكساندرا 🔱")

# عرض رسالة ترحيب فخمة
st.write("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.header("مرحباً بكِ في عصر السيادة الرقمية")
    st.info("هذا النظام محمي بشفرات 'ألكساندرا' الخاصة. الوصول مسموح فقط للنخبة.")
    
    # إضافة زر تفاعلي "لتفعيل القوة"
    if st.button("تفعيل بروتوكول الاحتفال 🚀"):
        st.balloons()
        st.snow()
        st.success("تم تفعيل النظام بنجاح! أنتِ الآن تديرين الإمبراطورية.")

# إضافة رسم بياني فخم ومتحرك
import pandas as pd
import numpy as np

st.write("---")
st.subheader("📊 مراقبة نبض الإمبراطورية (بيانات حية)")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['الطاقة', 'الأمن', 'السيطرة'])
st.line_chart(chart_data)

st.sidebar.title("إعدادات الإمبراطورة")
st.sidebar.write("المسؤولة: Alexandra")
st.sidebar.write("الموقع: تونس 🇹🇳")
st.sidebar.button("تسجيل الخروج الآمن")

