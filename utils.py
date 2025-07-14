import streamlit as st
import os

# Replace this with your real office IPs or IP ranges
ALLOWED_IPS = ["192.168.0.", "10.0.0."]

def is_allowed_ip():
    try:
        ip = st.runtime.scriptrunner.get_script_run_ctx().request.remote_ip
    except:
        ip = os.getenv("REMOTE_ADDR", "")  # fallback for Streamlit Cloud

    for allowed in ALLOWED_IPS:
        if ip.startswith(allowed):
            return True
    return False
