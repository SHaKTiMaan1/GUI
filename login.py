import sys
import bcrypt
import pymongo
import sqlite3
"""Connection String"""
client = pymongo.MongoClient(
    "mongodb+srv://CCI:root@cluster0.4gzmr.mongodb.net/CARE?retryWrites=true&w=majority")
db = client["Jhansi"]
col = db["cciemployees"]
"""Getting Credentials"""
print("Email: ",end="")
email = input().strip()
pswd = input().strip()
"""Searching for document with the specified CCI Id"""
query = {"email": f"{email}"}
doc = col.find(query)
for x in doc:
    hashp = x["password"]
    hashp = hashp.encode('utf-8')
    cci_id = x["cci_id"]
"""Validating Password"""
pswd = pswd.encode('utf-8')
if(bcrypt.checkpw(pswd, hashp)):
    print("Login Successful")
    f = open("CCI.txt","w+")
    f.write(cci_id+"\n")
    f.close()
else:
    print("Wrong Credentials")












































































