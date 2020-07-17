import sys
import bcrypt
import re
from getpass import getpass
import pymongo
import sqlite3
"""Connection String"""
client = pymongo.MongoClient(
    "mongodb+srv://CCI:root@cluster0.4gzmr.mongodb.net/CARE?retryWrites=true&w=majority")
db = client["CARE"]
col = db["cciemployees"]
"""Getting Credentials"""
print("Email: ",end="")
email = input().strip()
pswd = getpass("Password: ", sys.stderr)
"""Searching for document with the specified CCI Id"""
query = {"email": f"{email}"}
doc = col.find(query)
for x in doc:
    hashpass = x["password"]
    hashpass = hashpass.encode('utf-8')
    cci_id = x["cci_id"]
"""Validating Password"""
pswd = pswd.encode('utf-8')
if(bcrypt.checkpw(pswd, hashpass)):
    print("Login Successful")
    f = open("CCI_ID.txt","w+")
    f.write(cci_id)
    f.close()
else:
    print("Wrong Credentials")
    

    
