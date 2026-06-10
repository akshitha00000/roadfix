import sqlite3

def create_table():
    conn = sqlite3.connect("complaints.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        district TEXT,
        location TEXT,
        description TEXT,
        image_path TEXT,
        status TEXT,
        completion_note TEXT,
        repaired_image TEXT
    )
    """)

    conn.commit()
    conn.close()

create_table()