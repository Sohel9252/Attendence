import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "data/attendance.db")
ALLOWED_IP_PREFIXES = os.getenv("ALLOWED_IPS", "192.168.0.,10.0.0.").split(",")
