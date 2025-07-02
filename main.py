import streamlit as st
st.title("Stremlit Application")
st.write("creating a simple web application using streamlit")
name=st.text_input("Enter your name")
if st.button("submit"):
  st.write("hello", name, "welcome to strwamlit")
