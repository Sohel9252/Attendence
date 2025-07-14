import streamlit as st
import pandas as pd
import sqlite3

DB_PATH = 'data/attendance.db'

def show_admin_dashboard():
    st.subheader("📊 Admin Dashboard - Attendance Records")

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT username, date, time FROM attendance ORDER BY date DESC, time DESC", conn)
    conn.close()

    if df.empty:
        st.info("No attendance records found.")
        return

    st.dataframe(df, use_container_width=True)

    with st.expander("📅 Filter by Date"):
        selected_date = st.date_input("Select a date to filter", key="admin_date_filter")
        filtered_df = df[df['date'] == selected_date.strftime('%Y-%m-%d')]
        if not filtered_df.empty:
            st.write(f"Records for {selected_date.strftime('%Y-%m-%d')}:")
            st.dataframe(filtered_df, use_container_width=True)
        else:
            st.warning("No records found for the selected date.")
