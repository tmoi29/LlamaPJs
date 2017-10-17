'''
Team Llama PJs
Tiffany Moi and Leo Liu
SoftDev1 pd7
HW10 -- Average
2017-10-17
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="info.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

comm = "SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id;"
student_list = c.execute(comm)
#print(student_list)

def info(stuff):
    nums = 0
    count = 0
    name = ""
    idnum = 0
    for thing in stuff:
        name = thing[0]
        idnum = thing[1]
        nums += thing[2]
        count += 1
    print "Name: " +  name + " ID: " + str(idnum) + " Avg: " + str(nums/count)
    
idnum = 1
entries = []
for student in student_list:
    if student[1] == idnum:
        entries.append(student)
    else:
        entry = student
        info(entries)
        entries = []
        entries.append(entry)
        idnum += 1
info(entries)


#==========================================================
db.commit() #save changes
db.close()  #close database


