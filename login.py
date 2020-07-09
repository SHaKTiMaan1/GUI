import sys
import bcrypt
import re
from getpass import getpass
import pymongo
if __name__ == "__main__":
    client = pymongo.MongoClient(
        "mongodb+srv://CCI:root@cluster0.4gzmr.mongodb.net/Jhansi?retryWrites=true&w=majority")
    db = client["Jhansi"]
    col = db["ccis"]
    print("CCI ID: ",end="")
    username = input().strip()
    pswd = getpass("Password: ", sys.stderr)
    query = {"cci_id": f"{username}"}
    doc = col.find(query)
    for x in doc:
        hashpwd = x["pwd"]
        print(hashpwd)
    valid = bcrypt.checkpw(pswd.encode(), hashpwd)
    if(valid):
        print("Login Successful")
    else:
        print("Wrong Credentials")
    

    
