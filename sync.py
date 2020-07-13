import pymongo
import sqlite3
from login import cci_id

client_web = pymongo.MongoClient(
    "mongodb+srv://CCI:root@cluster0.4gzmr.mongodb.net/Jhansi?retryWrites=true&w=majority")
db = client_web["Jhansi"]
col = db["children"]

conn = sqlite3.connect("child.db")
c = conn.cursor()
c = conn.execute('''SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'details' ;''')

if c.fetchone()[0] != 'details':
    conn.execute('''CREATE TABLE details 
                    (C_ID INT PRIMARY KEY NOT NULL, 
                    NAME TEXT NOT NULL, 
                    AGE INT NOT NULL, 
                    DOR TEXT NOT NULL,
                    GENDER CHAR(1) NOT NULL,
                    WITNESS CHAR(25) NOT NULL); ''')
else:
    pass
    


c = conn.execute('''SELECT C_ID FROM details;''')
rows = c.fetchall()
ls = []
for row in rows:
    ls.append(row[0])
print(ls)

doc = col.find({"cci_id": f"{cci_id}"}, {
               "_id": 0, "cci_name": 0, "cci_id": 0, "cci_address": 0, "__v":0})
for x in doc:
    if(x["C_Id"] not in ls):
        c.execute('''INSERT INTO details(NAME, C_ID, AGE, DOR, GENDER, WITNESS)
                    VALUES(:name,:C_Id, :age, :reg_date, :gender, :witness)''',x)
    else:
        pass


conn.commit()
conn.close()
