'''
Team Llama PJs
Tiffany Moi and Leo Liu
SoftDev1 pd7
HW10 -- Average
2017-10-17
'''
 
import sqlite3   #enable control of an sqlite database

f="info.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()         #facilitate db ops
outputComms = []        #start a list of commands to execute at the end
comm = "CREATE TABLE peeps_avg(id INTEGER, avg NUMERAL)"
c.execute(comm)

comm = "SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id;"
student_list = c.execute(comm)
#print(student_list)

def info(student):
    nums = 0
    count = 0
    name = student[0][0]
    idnum = student[0][1]
    for grade in student:
        ''' 
        debug code================
        print "name:  "
        print grade[0]
        print "ID:    "
        print grade[1]
        print "grade: "
        print grade[2]
        end of debug code=========
        '''
        nums += grade[2]
        count += 1
    avg = str(nums/count)
    print "Name: " +  name + "      \tID: " + str(idnum) + "\t\tAvg: " + avg
    nums = 0
    command = "INSERT INTO peeps_avg VALUES({id},{avg})".format(id=str(idnum),avg=avg)
    outputComms.append(command)
    
idnum = 1
entries = []
#separate student_list into individual students, and process it
for student in student_list:
    if student[1] == idnum:
        entries.append(student)
    else:
        entry = student
        info(entries)
        entries = []
        entries.append(entry)
        idnum += 1

#needed for the last student
info(entries)
for command in outputComms:
    print command
    c.execute(command)

averages = c.execute("SELECT * FROM peeps_avg")
for average in averages:
    print average


#==========================================================
#shouldn't be saving any changes, as this is read-only
db.commit() #save changes
db.close()  #close database


