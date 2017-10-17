import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="info.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

comm = "SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id;"
student_list = c.execute(comm)
#print(student_list)
idnum = 1
avg = 0
count = 0
name = ""
for student in student_list:
    print idnum
    print student[1]
    if student[1] == idnum:
        avg += student[2]
        count += 1
        name = student[0]
    elif count == 0:
        count = 0
        avg = 0
        idnum += 1
    else:
        print "Name: " + name + " ID: " + str(idnum) + " Avg: " + str(avg/count)
        count = 0
        avg = 0
        idnum += 1
        

#==========================================================
db.commit() #save changes
db.close()  #close database


