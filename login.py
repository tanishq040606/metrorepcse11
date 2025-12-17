import streamlit as st
st.header("LOGIN FORM")
name=st.text_input("Enter Name:")
password=st.text_input("Enter Password:", type="password")
if st.button("submit"):
    if name=="tani" and password=="123":
        st.success("LOGIN DONE!")
        st.toast()
    else:
        st.error("Invalid Login Details")
    
