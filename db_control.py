import csv

from db import get_db


def insert_details():
    db = get_db()
    cursor = db.cursor()
    a_file = open("data.csv")
    rows = csv.reader(a_file)
    cursor.executemany("INSERT INTO freshers VALUES (?, ?, ?, ?, ?)", rows)
    cursor.execute("SELECT * FROM freshers")
    return cursor.fetchall()
