# 📁 File: app/main.py

import streamlit as st
from app.auth import login_user, logout_user
from app.attendance import mark_attendance
from app.admin_dashboard import show_admin_dashboard
from app.utils import is_allowed_ip
import os

# --------- PAGE CONFIG ---------
st.set_page_config(page_title="Office Attendance App", layout="centered")

# --------- SESSION STATE INIT ---------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'role' not in st.session_state:
    st.session_state.role = None

# --------- IP CHECK ---------
if not is_allowed_ip():
    st.error("Access Denied. You are not on the office network.")
    st.stop()

# --------- APP LOGIC ---------

def main():
    st.title("🏢 Office Attendance System")

    if not st.session_state.logged_in:
        login_user()
    else:
        st.success(f"Welcome, {st.session_state.username}!")
        st.button("Logout", on_click=logout_user)

        if st.session_state.role == "admin":
            show_admin_dashboard()
        else:
            mark_attendance()

if __name__ == '__main__':
    main()
