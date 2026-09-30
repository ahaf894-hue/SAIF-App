import streamlit as st
import pandas as pd
import time
import random

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="نظام سيف - SAIF Security Platform",
    page_icon="🛡️",
    layout="wide"
)

# شريط العنوان العلوي
st.title("🛡️ نظام سيف (SAIF) - منصة الرصد والتحليل اللحظي للهجمات")
st.caption("System for Artificial Intelligence-driven Filtering/Detection | إبداع 2026")
st.markdown("---")

# القائمة الجانبية
st.sidebar.header("⚙️ لوحة التحكم")
menu = st.sidebar.radio("الانتقال إلى:", ["فحص الملفات (File Scanner)", "مراقبة الشبكة اللحظية (Live Traffic)", "عن النظام"])

# 1. قسم فحص الملفات وقواعد البيانات
if menu == "فحص الملفات (File Scanner)":
    st.header("🔍 فحص الملفات والسجلات (PCAP / CSV Datasets)")
    st.write("قم برفع ملفات حركة الشبكة لفحصها واكتشاف الثغرات والهجمات بواسطة نموذج الذكاء الاصطناعي.")
    
    uploaded_file = st.file_uploader("اختر ملف حركة المرور أو قاعدة البيانات", type=["csv", "pcap", "log"])
    
    if uploaded_file is not None:
        st.success(f"تم تحميل الملف بنجاح: {uploaded_file.name}")
        
        if st.button("بدء التحليل باستخدام نموذج SAIF"):
            with st.spinner('جاري تحليل خصائص حزم البيانات واستخراج الميزات...'):
                time.sleep(2) # محاكاة معالجة الذكاء الاصطناعي
            
            st.subheader("📊 نتائج الفحص")
            
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("إجمالي السجلات المفحوصة", "15,420", "+100%")
            col2.metric("حركة مرور طبيعية", "14,890", "96.5%")
            col3.metric("الهجمات المكتشفة", "530", "3.5%", delta_color="inverse")
            col4.metric("زمن الاستجابة", "0.12 ثانية", "Real-time")
            
            st.markdown("---")
            st.subheader("⚠️ التهديدات المكتشفة التفصيلية")
            
            threat_data = pd.DataFrame({
                "Timestamp": ["10:42:01", "10:42:05", "10:42:12", "10:42:18"],
                "Source IP": ["192.168.1.105", "10.0.0.45", "172.16.0.12", "192.168.1.201"],
                "Threat Type": ["DDoS Attack", "Zero-Day Anomaly", "Port Scan", "SQL Injection"],
                "Confidence": ["99.4%", "94.8%", "98.1%", "97.6%"],
                "Action Taken": ["Blocked 🚫", "Isolated ⚠️", "Blocked 🚫", "Blocked 🚫"]
            })
            st.dataframe(threat_data, use_container_width=True)

# 2. قسم المراقبة الحية
elif menu == "مراقبة الشبكة اللحظية (Live Traffic)":
    st.header("⚡ المراقبة اللحظية للشبكة (Real-Time Behavioral Engine)")
    
    col_status, col_btn = st.columns([3, 1])
    with col_status:
        st.info("حالة الحارس الرقمي: **نشط ويعمل بالتحليل السلوكي**")
    
    st.subheader("📈 معدل حزم البيانات وقوة التهديدات")
    chart_data = pd.DataFrame({
        'Normal Traffic (Packet/s)': [random.randint(800, 1200) for _ in range(20)],
        'Detected Anomaly (Threats)': [random.randint(0, 15) for _ in range(20)]
    })
    st.line_chart(chart_data)

# 3. عن النظام
else:
    st.header("ℹ️ حول مشروع سيف (SAIF)")
    st.write("""
    * **اسم المشروع:** سيف (SAIF)
    * **مجال الابتكار:** الذكاء الاصطناعي في الأمن السيبراني.
    * **قواعد البيانات المعتمدة:** CICIDS2017, UNSW-NB15, NSL-KDD.
    * **الميزة التنافسية:** التحول من Signature-based إلى Behavioral Anomaly Detection للحد من زمن الكشف لأقل من 0.5 ثانية.
    """)
