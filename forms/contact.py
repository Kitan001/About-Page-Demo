import re
from urllib import response
import streamlit as st
import requests



WEBHOOK_URL = st.secrets["WEBHOOK_URL"]


def isValidEmail(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("contact_form"):
        name=st.text_input("First Name")
        email=st.text_input("Email Address")
        message=st.text_area("Your Message")
        submit_button=st.form_submit_button("Send Message")

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email Service is not set up. Please try agaim later.", icon ="XX")
                st.stop()
            if not name:
                st.error("Please provide your name")            
                st.stop()
            if not email:
                st.error("Please provide your email address")
                st.stop()
            if not isValidEmail(email):
                st.error("Please Provide a valid email address")
                st.stop()
            if not message:
                st.error("Please input your message")
                st.stop()
            
            data = {"email":email, "name":name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)
            if response.status_code ==200:
                st.success("Your message has been sent!")
            else:
                st.error("There was an error sending your message. Please try again later")
            