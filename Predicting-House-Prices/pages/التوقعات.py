import streamlit as st
from setings.Prediction_Setings import *
import warnings
warnings.simplefilter("ignore")

def predictions():
    st.set_page_config(page_title="التوقعات", layout="wide", initial_sidebar_state="auto")
    st.write("""
    <style>
        body {
        direction: rtl;
        }
    </style>
    """, unsafe_allow_html=True
    )

    category = st.sidebar.selectbox("نوع المودل", ["XGboost"])
    if category == "XGboost":
        st.write("### نسبة توقع `XGboost` : من `75%` الى`95%`", )



    city = st.selectbox("المدينة :", All_Citys())
    district = st.selectbox("الحي", district_of_city(city))
    front = st.selectbox("الواجهة :", All_front())
    rooms = st.number_input("عدد الغرف :", min_value=1, max_value=20, value=4)
    living_rooms = st.number_input("عدد الصالات :", min_value=1, max_value=20, value=2)
    bath_rooms = st.number_input("عدد دورات المياة :", min_value=1, max_value=20, value=2)
    street_width = st.number_input("عرض الشارع :", min_value=1, max_value=100, value=50)
    level = st.number_input("الدور :", min_value=1, max_value=20, value=10)
    age = st.number_input("العمر :", min_value=1, max_value=30, value=15)
    kitchen = st.selectbox("المطبخ :", True_and_False_option())
    garage = st.selectbox("قراج :", True_and_False_option())
    elevator = st.selectbox("المصعد :", True_and_False_option())
    dimension_1 = st.number_input("الطول : ", min_value=1, max_value=100, value=20) 
    dimension_2 = st.number_input("العرض: ", min_value=1, max_value=100, value=20)
    area = st.number_input("المساحة :", min_value=1, max_value=10000, value=400)

    if st.button("توقع السعر"):
        if category == "XGboost":
            prediction = XGB_predict([City_value(city), district_value(district), front_value(front), rooms, living_rooms, bath_rooms,
                street_width, level, age, True_and_False(kitchen), True_and_False(garage), True_and_False(elevator),
                area, dimension_1, dimension_2])
            st.success(f"السعر المتوقع : {prediction} ريال سعودي")
            

predictions()