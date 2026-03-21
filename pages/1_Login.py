import streamlit as st

from src.utils.logger_config import logger

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "admin":
        st.session_state["authenticated"] = True
        st.success("Logged in!")
        logger.info("User logged in successfully.")

    else:
        st.error("Invalid credentials")
        logger.warning("Failed login attempt.")
