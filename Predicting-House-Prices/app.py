from PIL import Image
import streamlit as st
from streamlit.logger import get_logger
import streamlit.components.v1 as components
import os

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(page_title="الصفحة الرئيسية", layout="wide", initial_sidebar_state="auto")

    st.write("""
    <style>
        body {
        direction: rtl;
        }
    </style>
    """, unsafe_allow_html=True
    )

    st.write(
    """
    #  مرحبا بكم في مشروع توقع اسعار الشقق في المملكة العربية السعودية
    """
    )

    file = "/Logo/logo.png"
    path = os.getcwd() + file

    image = Image.open(path)
    st.image(image, width=250)

    st.write(
    """
    ## يساعدك هذا المشروع في توقع اسعار الشقق بدقة عالية
    ### رؤيتنا 
    ##### ان نساعد كل من يبحث عن شقه و اصحاب العقارات في اتخاذ القرار وتحديد سعر المسكن  باستخدام تعلم الالة و لتحقيق رؤية المملكة في تطوير الذكاء الإصطناعي وتطبيقاته   
    """
    )                                                                        

if __name__ == "__main__":
    run()