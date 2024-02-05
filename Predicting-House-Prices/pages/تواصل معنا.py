import streamlit as st

# Create a function for the contact page
def contact():
    st.set_page_config(page_title="تواصل معنا", layout="wide", initial_sidebar_state="auto")
    
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
        إذا كان لديك أي أسئلة أو ملاحظات حول مشروعنا ، فلا تتردد في الاتصال بنا
        """
        )
    
    st.write(
        """
        يمكنك التواصل معنا عبر البريد الإلكتروني على ` contact@mlproject.com `
        أو ملء النموذج أدناه.
        """
    )

    name = st.text_input("الاسم")
    email = st.text_input("البريد الألكتروني")
    message = st.text_area("المحتوى")

    if st.button("ارسال"):
        st.success("شكرا لك. سوف يتم الرد عليك في اقرب وقت")

contact()