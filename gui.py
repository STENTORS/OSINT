import streamlit as st
from backend import *

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Micro+5&display=swap');

body {
  font-family: "Micro 5", serif;
  font-weight: 400;
  font-style: normal;
  color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("~~(__^·>")

c1, c2 = st.columns([1,1])

with c1:
    with st.form("personalDetailsForm"):
        firstName = st.text_input("First Name", placeholder="Name")
        lastName = st.text_input("Last Name", placeholder="Name")
        email = st.text_input("Email", placeholder="Email")
        phone = st.text_input("Phone Number", placeholder="Phone")
        submitted = st.form_submit_button('Submit')

with c2:
    st.subheader("Personal Details")
    st.image("img/Daghtuj.png", caption="Silly Dog")

st.divider()


c3, c4 = st.columns([1,1])

with c3:
    st.subheader("Other Details")
    st.image("img/car.png", caption="Silly Car")

with c4:
    with st.form("otherDetailsForm"):
        userName = st.text_input("Username", placeholder="username")
        profession = st.text_input("profession", placeholder="profession")
        company = st.text_input("company", placeholder="company")
        ip = st.text_input("IP Address", placeholder="IP")
        st.form_submit_button('Submit')

st.divider()
if submitted:
    showBreach = interface(firstName, lastName, email, phone)
else:
    showBreach = ""
    
if showBreach:
    if isinstance(showBreach, list) and len(showBreach) > 0:
        st.subheader("Breaches Found 🔓")
        for breach in showBreach:
            st.markdown(f"- {breach['title']}")
    else:
        st.write("No breaches found. Your data is safe! 🔒")
else:
    st.write("")  # Handle empty state
