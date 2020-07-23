import sqlite3
from datetime import date
import pymongo
import socket
import time

#Getting CCI ID through file
f = open("CCI.txt", "r")
lines = list(f)
cci_id = lines[0].rstrip("\n")
f.close()

#Getting system date
d = date.today().strftime('%d-%m-%Y')

#Connecting to sqlite database
conn = sqlite3.connect('child.db')
c = conn.cursor()

#List which stores data to be synced
l = []

c.execute("SELECT COUNT(DISTINCT DATE) FROM attendance WHERE SYNCED = 'False' AND DATE != '%s'  ", % d)
for row in c.fetchall():
    n = row[0]

for i in range(n):
    c.execute("SELECT DATE FROM attendance WHERE SYNCED = 'False' AND DATE != '%s'  ", % d")
    for row in c.fetchone():
        working_date = row[0]
        break
    ls = []
    c.execute(''' SELECT DATE, C_ID, FNAME, LNAME, ATTEND
                FROM attendance 
                INNER JOIN details ON attendance.C_ID = details.C_ID 
                WHERE SYNCED = 'False' AND DATE != '%s'  ''', % d)
    for row in c.fetchall():
        if  row[0] == working_date :
            if row[4] == "True":
                present = True
            else:
                present = False
            child_obj = {
                "C_Id" : row[1],
                "firstName" : row[2],
                "lastName" : row[3],
                "present" : present
            }
            ls.append(child_obj)
    #The list ls is completed till here
    attendance_obj = {
        "date" : working_date,
        "data" : ls
    }
    l.append(attendance_obj)
    c.execute("UPDATE attendance SET SYNCED = 'True' WHERE DATE = '%s'" %working_date)

while len(l)>0:
    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress != "127.0.0.1":
        #Connecting to the mongodb atlas
        client_web = pymongo.MongoClient("mongodb+srv://CCI:root@cluster0.4gzmr.mongodb.net/Jhansi?retryWrites=true&w=majority")
        db = client_web["Jhansi"]
        col = db["ccis"]
        query = {"cci_id": f"{cci_id}"}
        for obj in l :
            result = col.update_one(query, {'$push': {"attendance": obj}})
        if result.modified_count > 0:
            l.clear()
    
    else:
        time.sleep(20)

            
