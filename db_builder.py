'''
Tiffany Moi
SoftDev1 pd7
HW9 -- No Treble
2017-10-16
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="info.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
command = "CREATE TABLE courses(code TEXT, mark INTEGER, id iNTEGER);"
c.execute(command)    #run SQL statement

#open le file
f = csv.DictReader(open("courses.csv"))

#loopy loop through data entries
for row in f:
    code = '"' + row["code"] + '"'
    mark = int(row['mark'])
    idnum = int(row['id'])
    command = "INSERT INTO courses VALUES(%s, %d, %d);" %(code, mark, idnum)
    c.execute(command)    #run SQL statement

#==========================================================
#db.commit() #can't commit here or else it won't run the rest


#rinse n repeat

#==========================================================
command = "CREATE TABLE peeps(name TEXT, age INTEGER, id iNTEGER);"
c.execute(command)    #run SQL statement

#open le file
f = csv.DictReader(open("peeps.csv"))

#loopy loop through data entries
for row in f:
    name = '"' + row["name"] + '"'
    age = int(row['age'])
    idnum = int(row['id'])
    command = "INSERT INTO peeps VALUES(%s, %d, %d);" %(name, age, idnum)
    c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes

db.close()  #close database


