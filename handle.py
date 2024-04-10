import sqlite

def handle():
    con = sqlite.connect("table.db")
    cur = con.cursor()

handle()

