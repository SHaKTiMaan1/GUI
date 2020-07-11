import pymongo
import sqlite3
import login

client_web = pymongo.MongoClient(
    "mongodb+srv://CCI:root@cluster0.4gzmr.mongodb.net/Jhansi?retryWrites=true&w=majority")
db = client["Jhansi"]

conn = sqlite3.connect("child.db")
c = conn.cursor()
c.execute()
conn.commit()
conn.close()