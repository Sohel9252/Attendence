import sqlite3

conn = sqlite3.connect("data/attendance.db")
c = conn.cursor()

# Create user table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
''')

# Create attendance table
c.execute('''
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    date TEXT,
    time TEXT
)
''')

# Optional: Add an admin user
import hashlib
admin_pass = hashlib.sha256("admin123".encode()).hexdigest()
c.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)",
          ("admin", admin_pass, "admin"))

conn.commit()
conn.close()

print("✅ Database initialized.")
