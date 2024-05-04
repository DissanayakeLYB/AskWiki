import streamlit as st

st.set_page_config(
    page_title = "Welcome",
    page_icon = "🧐",
    menu_items = {
        "Report a Bug" : "mailto:lasithdissanayake.official@gmail.com",
        "About" : "https://dissanayakelyb.github.io/LasithDissanayake.github.io/"
    }
)

st.title("How-To")

st.subheader("Step 01 - Create an account on Groq https://groq.com/.")

st.subheader("Step 02 - Get your free Groq API key from https://console.groq.com/keys.")

st.subheader("Step 03 - Create a new API key and save it.")

st.subheader("Step 04 - Paste it in 'Enter the GROQ API' in 'From Expert'.")

st.subheader("Step 05 - Select a model of your Choice.")

st.subheader("Step 06 - Use the chat input and embrace the ultra fast responses.")

st.write("&copy; Lasith Dissanayake | 2024")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)