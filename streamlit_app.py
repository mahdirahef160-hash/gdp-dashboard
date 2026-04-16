import streamlit as st
import hashlib
import hmac
import time
import uuid
import pandas as pd
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="Alexandra Empire Core", layout="wide")

# ==========================================
# 1. نظام الحماية (Security Shield)
# ==========================================
class QuantumShield:
    def __init__(self):
        if 'master_secret' not in st.session_state:
            st.session_state.master_secret = str(uuid.uuid4()).encode()
        
    def generate_token(self, payload: str) -> str:
        return hmac.new(st.session_state.master_secret, payload.encode(), hashlib.sha3_512).hexdigest()

    def verify_token(self, payload: str, token: str) -> bool:
        return hmac.compare_digest(self.generate_token(payload), token)

# ==========================================
# 2. واجهة الإمبراطورية (The Dashboard)
# ==========================================
def main():
    shield = QuantumShield()
    
    st.title("🛡️ Alexandra Empire: Command & Control")
    st.markdown("---")

    # تقسيم الشاشة إلى أعمدة
    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("🎮 مركز القيادة")
        user_input = st.text_input("أدخل أمر الإمبراطورية:", "Initialize Satellite")
        submit = st.button("تنفيذ الأمر")
        
        st.markdown("---")
        st.subheader("⚠️ سجلات الرقيب (Sentinel)")
        if 'alerts' not in st.session_state:
            st.session_state.alerts = []
        
        for alert in st.session_state.alerts[-5:]:
            st.error(alert)

    with col2:
        st.header("📊 مراقبة حركة البيانات (Traffic)")
        if 'traffic_logs' not in st.session_state:
            st.session_state.traffic_logs = []

        if submit:
            # محاكاة مرور الأمر عبر الـ Bus والـ Sentinel
            token = shield.generate_token(user_input)
            
            # فحص أمني بسيط (Sentinel logic)
            forbidden = ["DROP", "DELETE", "root", "BYPASS"]
            is_malicious = any(p in user_input.upper() for p in forbidden)
            
            log_entry = {
                "Time": datetime.now().strftime("%H:%M:%S"),
                "Sender": "COMMAND_CENTER",
                "Payload": user_input,
                "Token": f"{token[:15]}...",
                "Status": "❌ BLOCKED" if is_malicious else "✅ CLEARED"
            }
            
            st.session_state.traffic_logs.append(log_entry)
            
            if is_malicious:
                st.session_state.alerts.append(f"تنبيه: محاولة اختراق بنمط محظور في الأمر: {user_input}")

        # عرض سجل البيانات
        if st.session_state.traffic_logs:
            df = pd.DataFrame(st.session_state.traffic_logs)
            st.table(df.tail(10))

    # حالة النظام في التذييل
    st.sidebar.header("⚙️ حالة النواة")
    st.sidebar.success("النزاهة: سليمة (Integrity OK)")
    st.sidebar.info(f"معرف الجلسة: {uuid.uuid4().hex[:8]}")
    if st.sidebar.button("إعادة تشغيل النظام"):
        st.session_state.traffic_logs = []
        st.session_state.alerts = []
        st.rerun()

if __name__ == "__main__":
    main()
            
    
            
    
