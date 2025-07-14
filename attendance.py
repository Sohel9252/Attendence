import streamlit as st
import sqlite3
from datetime import datetime

DB_PATH = 'data/attendance.db'

def mark_attendance():
    st.subheader("📅 Mark Your Attendance")
    today = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")

    if already_marked(st.session_state.username, today):
        st.info("✅ You have already marked your attendance today.")
        return

    if st.button("Mark Attendance"):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO attendance (username, date, time) VALUES (?, ?, ?)",
                  (st.session_state.username, today, time_now))
        conn.commit()
        conn.close()
        st.success("🎉 Attendance marked successfully!")

def already_marked(username, date):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM attendance WHERE username = ? AND date = ?", (username, date))
    result = c.fetchone()
    conn.close()
    return result is not None
