#HackRU - Python Methods to manipulate MySQL Database with details of students
"""
For this program to work, you need to have MySQL configured properly with a username and password. Replace defaultuser and pwd_here with the configured details.
You will need to use pip to install PIL and MySQL.connector, commands for that:

python3 -m pip install --upgrade Pillow
python3 -m pip install mysql-connector-python

"""

import mysql.connector as mc
import base64
import io
from PIL import Image

try:
    mydb = mc.connect (host = "localhost", user = "defaultuser", passwd = "pwd_here")
    mycur = mydb.cursor()

except:
    print("Connection failed")

def CreateDBTable():

    mycur.execute("CREATE DATABASE STUDENTDB")

    #will not work if database with same name already exists, so add a try except for that case as needed
    """
    try:
        mycur.execute("CREATE DATABASE STUDENTDB")
    except:
        print("Table already exists") #replace print statement if required
    """
    
    mycur.execute("USE STUDENTDB")
    
    #will not work if table already exists, so make use of try except if needed
    mycur.execute("CREATE TABLE INFO (NETID varchar(6), Name varchar(25), img LONGBLOB, PRIMARY KEY (NETID) )")

#need to have a valid database and table, provide arguments/parameters to call function, all 3 arguments to be enclosed within single quotes ''
def InsertStudent(netid, studname, imgpath):

    file = base64.b64encode(open(imgpath, 'rb').read()) 
    args = (netid, studname , file) 
    query = 'INSERT INTO INFO VALUES(%s, %s, %s)'
    mycur.execute(query, args)
    mycur.commit()

#Delete student with specified netid
def DeleteStudentwNETID(netid):

    mycur.execute("DELETE FROM INFO WHERE NETID = '"+netid+"' ")

#Supply NETID to get image of Face
def GetFaceWithNetID(netid):

    mycur.execute("SELECT img FROM INFO WHERE NETID = '"+netid+"' ") #just check the quotes once if any issues
    data = mycur.fetchall()
    image = base64.b64decode(data[0][0])
    result = Image.open(io.BytesIO(image))
    #result contains image, the command result.show() can display image on screen, edit as required to get image in Flutter/another Python file

#Supply NETID to get Name
def GetNameWithNetID(netid):

    mycur.execute("SELECT Name FROM INFO WHERE NETID = '"+netid+"' ")
    data = mycur.fetchall()
    #data contains name, edit as required to get name in Flutter/another PY file








