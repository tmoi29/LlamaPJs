import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

peeps = []
with open('peeps.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print row
        peeps.append(row)
    print peeps

courses = []
with open('courses.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print row
        courses.append(row)
    print courses
    
#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

# Add check for existing table named peeps later...
c.execute("CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)")
for person in peeps:
    c.execute("INSERT INTO peeps VALUES(\"" + person['name'] + '",' + person['age'] + ',' + person['id'] + ')')

c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")
for grades in courses:
    c.execute("INSERT INTO courses VALUES(\"" + grades['code'] + '",' + grades['mark'] + ',' + grades['id'] + ')')

#==========================================================
db.commit() #save changes
db.close()  #close database


