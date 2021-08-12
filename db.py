import sqlite3

DATABASE_NAME = "freshers.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS freshers(
                id INTEGER PRIMARY KEY,
                name TEXT,
                college TEXT,
                city TEXT,
                Mentor TEXT
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
