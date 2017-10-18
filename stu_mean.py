'''
Team Llama PJs
Tiffany Moi and Leo Liu
SoftDev1 pd7
HW10 -- Average
2017-10-17
'''
 
import sqlite3   #enable control of an sqlite database
import csv

f="info.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()         #facilitate db ops


comm = "CREATE TABLE peeps_avg(id INTEGER, avg INTEGER)"
c.execute(comm)


def avg(grade_list, idnum):
    total = 0 #sum the grades
    count = 0
    name = ""
    #For each grade
    for entry in grade_list:
        name = entry[0]
        total += entry[2]
        count += 1
            
    #Show the student's info
    print  "Name: " + name +"\t ID: "+ str(idnum) + "\t Avg: " + str(total/count)
    return [idnum, total/count]

def insertVal(idnum, avg):
    #Put data into avg table
    comm = "INSERT INTO peeps_avg VALUES(" + str(idnum) + "," + str(avg) + ")"
    dup_curs = db.cursor() # so it doesn't break the loop
    dup_curs.execute(comm)
    db.commit()


def process():
    #Get all possible student IDs
    comm = "SELECT DISTINCT peeps.id FROM peeps, courses WHERE peeps.id = courses.id"
    ids = c.execute(comm)
    vals = []
    
    #For each student ID
    for num in ids:
        
        #Make a list of all the student's grades
        comm = "SELECT name, peeps.id, mark FROM peeps, courses WHERE courses.id = " + str(num[0]) + " AND peeps.id = " + str(num[0])
        dup_curs = db.cursor() # so it doesn't break the loop
        grade_list = dup_curs.execute(comm)
        vals.append(avg(grade_list, num[0]))
    return vals
        
def initialize():
    vals = process()
    for each in vals:
        insertVal(each[0], each[1])

initialize()

def updateVal(idnum, newAvg):
    comm = "UPDATE peeps_avg SET avg = " + str(newAvg) + " WHERE id = " + str(idnum)
    dup_curs = db.cursor() # so it doesn't break the loop
    dup_curs.execute(comm)
    
def updateAvg():
    print "\n\n NEW AVGS \n\n"
    vals = process()
    for each in vals:
        updateVal(each[0],each[1])
        
def addRows():
    #open le file
    f = csv.DictReader(open("courses.csv"))

    #loopy loop through data entries
    for row in f:
        code = '"' + row["code"] + '"'
        mark = int(row['mark'])
        idnum = int(row['id'])
        command = '''INSERT INTO courses(code, mark, id) 
        SELECT %s, %d, %d
        WHERE NOT EXISTS(SELECT id
        FROM courses 
        WHERE code = %s AND mark = %d AND id = %d)'''%(code, mark, idnum, code, mark, idnum)
        c.execute(command)    #run SQL statement

#TESTING....

#before updating
print "BEFORE UPDATE\n\n"
comm = "SELECT name, peeps.id, mark FROM peeps, courses WHERE courses.id = 1 AND peeps.id = 1" 
dup_curs = db.cursor() # so it doesn't break the loop
grade_list = dup_curs.execute(comm)

for grade in grade_list:
    print grade
    
#update
addRows()

#after updating

print "\n\nAFTER UPDATE\n\n"
comm = "SELECT name, peeps.id, mark FROM peeps, courses WHERE courses.id = 1 AND peeps.id = 1" 
dup_curs = db.cursor() # so it doesn't break the loop
grade_list = dup_curs.execute(comm)

for grade in grade_list:
    print grade
    
updateAvg()

#==========================================================
#shouldn't be saving any changes, as this is read-only
#db.commit() #save changes
db.close()  #close database


