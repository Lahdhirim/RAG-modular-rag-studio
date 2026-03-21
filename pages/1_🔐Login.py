import streamlit as st

from src.utils.logger_config import logger

# Set Streamlit page configuration
st.set_page_config(page_title="Login", layout="wide")
st.title("🔐 Login")

if st.session_state.get("authenticated", False):
    st.success("You are already logged in!")
    st.stop()

username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", type="password", placeholder="Enter your password")

if st.button("Login"):
    if username == "admin" and password == "securepassword":
        st.session_state["authenticated"] = True
        st.success("Logged in!")
        logger.info(f"User '{username}' logged in successfully.")

    else:
        st.error("Invalid credentials")
        logger.warning(f"Failed login attempt for user '{username}'.")
