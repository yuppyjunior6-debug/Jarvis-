
import streamlit as st

st.set_page_config(
    page_title="JARVIS",
    page_icon="🤖"
)

st.title("🤖 J.A.R.V.I.S")
st.subheader("Your Personal AI Assistant")

st.write("Hello Sir! I am JARVIS.")
st.write("I am ready to serve you.")

name = st.text_input("What should I call you?")

if name:
    st.success(f"Welcome, {name}! JARVIS is ready.")
