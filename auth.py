import streamlit as st
import sqlite3
import hashlib

DB_PATH = 'data/attendance.db'

def get_user(username):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT username, password, role FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()
    return result

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password, hashed):
    return hash_password(password) == hashed

def login_user():
    st.subheader("🔐 Login to continue")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        user = get_user(username)
        if user and check_password(password, user[1]):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = user[2]
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")

def logout_user():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.role = None
    st.success("Logged out successfully")
    st.experimental_rerun()
