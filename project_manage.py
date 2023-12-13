# import database module
import database
import random
import os,csv
from datetime import datetime
# start by adding the admin related code
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
# create an object to read an input csv file, persons.csv
project=[]
with open(os.path.join(__location__, 'project.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        project.append(dict(r))
# print(project)
advisor_invite=[]
with open(os.path.join(__location__, 'advisor_invite.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        advisor_invite.append(dict(r))
# print(advisor_invite)
member_invite=[]
with open(os.path.join(__location__, 'member_invite.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        member_invite.append(dict(r))
#print(member_invite)
login=[]
with open(os.path.join(__location__, 'login.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        login.append(dict(r))
print(login)
# create a 'persons' table
table=database.Table("persons",database.persons)
login_table=database.Table("login",login)
project_table=database.Table("project",project)
advisor_invite_table=database.Table("advisor_invite",advisor_invite)
member_invite_table=database.Table("member_invite",member_invite)

data=database.DB()
data.insert(table)
data.insert(login_table)
data.insert(project_table)
data.insert(advisor_invite_table)
data.insert(member_invite_table)
myperson=data.search("persons")
mylogin=data.search("login")
myproject=data.search("project")
myadvisorinvite=data.search("advisor_invite")
mymemberinvite=data.search("member_invite")

print(myperson)
print(mylogin)
# add the 'persons' table into the database

# create a 'login' table

# the 'login' table has the following keys (attributes):

# person_id
# username
# password
# role

# a person_id is the same as that in the 'persons' table
# let a username be a person's fisrt name followed by a dot and the first letter of that person's last name
# let a password be a random four digits string
# let the initial role of all the students be Member
# let the initial role of all the faculties be Faculty

# you create a login table by performing a series of insert operations; each insert adds a dictionary to a list

# add the 'login' table into the database

# add code that performs a login task; asking a user for a username and password; returning [person_id, role] if valid, otherwise returning None
def log_in():
    ask_username=input("Enter username : ")
    ask_password=input("Enter password : ")
    your_account=mylogin.filter(lambda x: x['username'] == ask_username).filter(lambda x: x['password'] == ask_password)
    if your_account.table!=[]:
        return(your_account.select(["role","ID"]))
    else:
        print("Username or password is incorrect")
        return None

# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [person_id, role] if valid, otherwise returning None

# make calls to the initializing and login functions defined above

# initializing()
while True:
    val1 = log_in()
    val=[val1[0]["ID"],val1[0]["role"]]
    print(val)
# END part 1

# CONTINUE to part 2 (to be done for the next due date)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

    if val[1]=="admin":
        # do something relate to admin
        while True:
            print("Options")
            print("Type 0 for Updating database")
            print("Type 1 for editing data")
            option=input("Select options : ")
            if option=="0":
                myFile = open('project.csv', 'w')
                writer = csv.writer(myFile)
                writer.writerow(['ID', 'title', 'lead',"member1","member2","advisor","status"])
                for dictionary in myproject.table:
                    writer.writerow(dictionary.values())
                myFile.close()
                myFile = open('member_invite.csv', 'w')
                writer = csv.writer(myFile)
                writer.writerow(['ID', 'user', 'response',"response_date"])
                for dictionary in mymemberinvite.table:
                    writer.writerow(dictionary.values())
                myFile.close()
                myFile = open('advisor_invite.csv', 'w')
                writer = csv.writer(myFile)
                writer.writerow(['ID', 'user', 'response',"response_date"])
                for dictionary in myadvisorinvite.table:
                    writer.writerow(dictionary.values())
                myFile.close()
                myFile = open('login.csv', 'w')
                writer = csv.writer(myFile)
                for dictionary in mylogin.table:
                    writer.writerow(dictionary.values())
                myFile.close()
                myFile = open('persons.csv', 'w')
                writer = csv.writer(myFile)
                for dictionary in myperson.table:
                    writer.writerow(dictionary.values())
                myFile.close()
                print("Database updated program closed")
                exit()
            if option=="1":
                select=input("Add or Delete someone data? : ")
                if select=="Add":
                    firstname=input("Input first name : ")
                    lastname=input("Input last name : ")
                    number=input("Input ID : ")
                    position=input("student or faculty : ")
                    myperson.table.append({"ID":number, "fist":firstname,"last":lastname,"type":position})
                    username=firstname+"."+lastname[0]
                    password=random.randint(1000,9999)
                    mylogin.table.append({"ID":number,"username":username,"password":password,"role":position})
                    print(f"{firstname} {lastname} successfully added to database")
                elif select=="Delete":
                    number=input("Input ID of someone you want to delete : ")
                    for i in range(len(myperson.table)):
                        if myperson.table[i]["ID"]==number:
                            myperson.table.pop(i)
                    for i in range(len(mylogin.table)):
                        if mylogin.table[i]["ID"]==number:
                            mylogin.table.pop(i)
                    for i in range(len(myproject.table)):
                        if myproject.table[i]["member1"]==number:
                            myproject.table[i]["member1"]==None
                        elif myproject.table[i]["member2"]==number:
                            myproject.table[i]["member2"]==None
                    print(f"Successfully deleted {number} from database")
    elif val[1]=="advisor":
        while True:
            print("Options")
            print("Type 1 for giving advices")
            print("Type 2 for approve project")
            print("Type 3 for viewing your own project")
            print("Type 0 for logging out")
            # do something relate to advisor
            ption=input("Select options : ")
            if option=="1":
                advice=input("Your advice : ")
                your_proj=myproject.filter(lambda x: x['advisor'] == val[0])
                for i in range(len(myproject.table)):
                    if myproject.table[i]["ID"]==your_proj.table[0]["ID"]:
                        myproject.table[i]["advices"]=advice
                        print("Your advices has been sent to group")
            elif option=="2":
                your_proj=myproject.filter(lambda x: x["advisor"]==val[0])
                for i in range(len(myproject.table)):
                    if myproject.table[i]["ID"]==your_proj.table[0]["ID"]:
                        if your_proj.table[0]["status"]=="Proposal pending approval":
                            approve=input("You want to approve this proposal? : ")
                            if approve=="Yes":
                                myproject[i]["status"]="Approved proposal"
                                print("Proposal approved")
                            elif approve=="No":
                                myproject[i]["status"]="starting"
                                print("Proposal denied")
                        elif your_proj.table[0]["status"]=="Final pending approval":
                            approve=input("You want to approve this proposal? : ")
                            if approve=="Yes":
                                myproject[i]["status"]="Approved final"
                                print("Final approved")
                            elif approve=="No":
                                myproject[i]["status"]="Passed evaluation"
                                print("Final denied")
            elif option=="3":
                your_proj=myproject.filter(lambda x: x["advisor"]==val[0])
                print(your_proj.table)
            elif option=="0":
                print("You logged out")
                break
    elif val[1]=="lead":
        while True:
            # do something relate to lead
            print("Options")
            print("Type 1 for inviting members")
            print("Type 2 for asking for advisors")
            print("Type 3 for submit proposal")
            print("Type 4 for release prototype")
            print("Type 5 for submit project")
            print("Type 6 for consulting advisors")
            print("Type 0 for logging out")
            option=input("Select options : ")
        # if option=="1":
        #     print("Creating project...")
        #     proj_name=input("Please input project name : ")
        #     for i in range(len(mylogin.table)):
        #         if mylogin.table[i]["person_id"]==val[0]:
        #             mylogin.add(i,"project",proj_name)
            if option=="1":
                user_invite=input("Send invite to (id) : ")
                for i in range(len(mylogin.table)):
                    if mylogin.table[i]["ID"]==user_invite:
                        if mylogin.table[i]["role"]=="student":
                            mylogin.add(i,"invite",f"pending from {val[0]}")
                            your_proj=myproject.filter(lambda x: x['lead'] == val[0])
                            proj_id=your_proj.table[0]["ID"]
                            mymemberinvite.table.append({"ID":proj_id,"user":user_invite,"response":"Pending","response_date":None})                    
            elif option=="2":
                user_invite=input("Send invite to (username) : ")
                for i in range(len(mylogin.table)):
                    if mylogin.table[i]["username"]==user_invite:
                        if mylogin.table[i]["role"]=="faculty" or mylogin.table[i]["role"]=="advisor":
                            mylogin.add(i,"invite",f"pending from {val[0]}")
                            your_proj=myproject.filter(lambda x: x['lead'] == val[0])
                            proj_id=your_proj.table[0]["ID"]
                            myadvisorinvite.table.append({"ID":proj_id,"user":user_invite,"response":"Pending","response_date":None})     
            elif option=="3":
                your_proj=myproject.filter(lambda x: x['lead'] == val[0])
                for i in range(len(myproject.table)):
                    if myproject.table[i]==your_proj.table[0]:
                        if your_proj.table[0]["status"]=="starting":
                            myproject.table[i]["status"]="Proposal pending arroval"
                            print("Your project are going to proposal pending approve phrase")
                        else:
                            print("Your project doesn't meet the condition")
            elif option=="4":
                your_proj=myproject.filter(lambda x: x['lead'] == val[0])
                for i in range(len(myproject.table)):
                    if myproject.table[i]==your_proj.table[0]:
                        if your_proj.table[0]["status"]=="Approved proposal":
                            myproject.table[i]["status"]="Release prototype"
                            print("Your project are going to prototype phrase")
                        else:
                            print("Your project doesn't meet the condition")           
            elif option=="5":
                your_proj=myproject.filter(lambda x: x['lead'] == val[0])
                for i in range(len(myproject.table)):
                    if myproject.table[i]==your_proj.table[0]:
                        if your_proj.table[0]["status"]=="Passed evaluation":
                            myproject.table[i]["status"]="Final pending arroval"
                            print("Your project are going to final pending approve phrase")
                        else:
                            print("Your project doesn't meet the condition") 
            elif option=="6":
                question=input("Your questions : ")
                your_proj=myproject.filter(lambda x: x['lead'] == val[0])
                for i in range(len(myproject.table)):
                    if myproject.table[i]["ID"]==your_proj.table[0]["ID"]:
                        myproject.table[i]["advices"]=question
                        print("Your question has been sent to advisor")
            elif option=="0":
                print("You logged out")
                break
    elif val[1]=="student":
        while True:
        # do something relate to student who are not member of any group
            print("Options")
            print("Type 1 for being a lead of the project")
            print("Type 2 for managing pending invites")
            print("Type 0 for logging out")
            option=input("Select options : ")
            if option=="1":
                print("Creating project...")
                proj_name=input("Please input project name : ")
                for i in range(len(mylogin.table)):
                    if mylogin.table[i]["ID"]==val[0]:
                        ID=random.randint(100000,999999)
                        myproject.table.append({"ID":ID,"title":proj_name,"lead":val[0],"member1":None,"member2":None,"advisor":None,"status":"starting"})
                        mylogin.add(i,"role","lead")
            elif option=="2":
                your_invite=mymemberinvite.filter(lambda x: x['user'] == val[0])
                if your_invite.table==[]:
                    print("You don't have any invite")
                else:
                    print(your_invite)
                    for i in range(len(your_invite.table)):
                        print("Manage your invite")
                        print(your_invite.table[i])
                        if your_invite.table[i]["response"]=="Pending":
                            response=input("Accept or Deny? : ")
                            if response=="Accept" or response=="accept":
                                accept_proj_id=your_invite.table[i]["ID"]                    
                                for j in range(len(myproject.table)):
                                    if myproject.table[j]["ID"]==accept_proj_id:
                                        if myproject.table[j]["member1"]==None:
                                            myproject.add(j,"member1",val[0])
                                            print("You accepted an invite and became second member")
                                            for k in range(len(mylogin.table)):
                                                if mylogin.table[k]["ID"]==val[0]:
                                                    mylogin.add(k,"role","member")
                                                    for l in range(len(mymemberinvite.table)):
                                                        if mymemberinvite.table[l]==your_invite.table[i]:
                                                            mymemberinvite.add(l,"response","Accept")
                                                            mymemberinvite.add(l,"response_date",datetime.now())
                                                        elif mymemberinvite.table[l] in your_invite.table:
                                                            mymemberinvite.add(l,"response","Deny")
                                                            mymemberinvite.add(l,"response_date",datetime.now())
                                        elif myproject.table[j]["member2"]==None:
                                            myproject.add(j,"member2",val[0])
                                            print("You accepted an invite and became third member")
                                            for k in range(len(mylogin.table)):
                                                if mylogin.table[k]["ID"]==val[0]:
                                                    mylogin.add(k,"role","member")
                                                    for l in range(len(mymemberinvite.table)):
                                                        if mymemberinvite.table[l]==your_invite.table[i]:
                                                            mymemberinvite.add(l,"response","Accept")
                                                            mymemberinvite.add(l,"response_date",datetime.now())
                                                        elif mymemberinvite.table[l] in your_invite.table:
                                                            mymemberinvite.add(l,"response","Deny")
                                                            mymemberinvite.add(l,"response_date",datetime.now())
                                        else:
                                            print("Group is already full")
                                        break
                            else:
                                print("You denied the invite")
                                for l in range(len(mymemberinvite.table)):
                                    if mymemberinvite.table[l]==your_invite.table[i]:
                                        mymemberinvite.add(l,"response","Deny")
                                        mymemberinvite.add(l,"response_date",datetime.now())
            elif option=="0":
                print("You logged out")
                break
    elif val[1]=="faculty":
        while True:
        # do something relate to faculty
            print("Options")
            print("Type 1 for viewing projects")
            print("Type 2 for evaluating prototype projects")
            print("Type 3 for managing pending invites")
            print("Type 0 for logging out")
            option=input("Select options : ")
            if option=="1":
                print(myproject.table)
            elif option=="2":
                prototype_proj=myproject.filter(lambda x: x['status'] == "Release prototype")
                for i in range(len(prototype_proj.table)):
                    while True:
                        your_rating=input("Rating score from 0-10 : ")
                        if isinstance(your_rating,int):
                            if your_rating>=0 and your_rating<=10:
                                break
                            else:
                                print("Please input the number in range 0-10")
                        else:
                            print("Please input the number in range 0-10")
                    for j in range(len(myproject.table)):
                        if prototype_proj.table[i]["ID"]==myproject.table[j]["ID"]:
                            if myproject.table[j]["Rating_1"]==None:
                                myproject.table[j]['Rating_1']=your_rating
                                print("Your rating has been submitted")
                            elif myproject.table[j]["Rating_2"]==None:
                                myproject.table[j]['Rating_2']=your_rating
                                print("Your rating has been submitted")
                            elif myproject.table[j]["Rating_3"]==None:
                                myproject.table[j]['Rating_3']=your_rating
                                print("Your rating has been submitted")
                            elif myproject.table[j]["Rating_4"]==None:
                                myproject.table[j]['Rating_4']=your_rating
                                print("Your rating has been submitted")
                            elif myproject.table[j]["Rating_5"]==None:
                                myproject.table[j]['Rating_5']=your_rating
                                myproject.table[j]["status"]="Passed evaluation"
                                print("Your rating has been submitted")
            elif option=="3":
                your_invite=myadvisorinvite.filter(lambda x: x['user'] == val[0])
                if your_invite.table==[]:
                    print("You don't have any invite")
                else:
                    print(your_invite)
                    for i in range(len(your_invite.table)):
                        print("Manage your invite")
                        print(your_invite.table[i])
                        if your_invite.table[i]["response"]=="Pending":
                            response=input("Accept or Deny? : ")
                            if response=="Accept" or response=="accept":
                                accept_proj_id=your_invite.table[i]["ID"]                    
                                for j in range(len(myproject.table)):
                                    if myproject.table[j]["ID"]==accept_proj_id:
                                        if myproject.table[j]["advisor"]==None:
                                            myproject.add(j,"advisor",val[0])
                                            print("You accepted an invite and became second member")
                                            for k in range(len(mylogin.table)):
                                                if mylogin.table[k]["ID"]==val[0]:
                                                    mylogin.add(k,"role","advisor")
                                                    for l in range(len(mymemberinvite.table)):
                                                        if myadvisorinvite.table[l]==your_invite.table[i]:
                                                            myadvisorinvite.add(l,"response","Accept")
                                                            myadvisorinvite.add(l,"response_date",datetime.now())
                                                        elif myadvisorinvite.table[l] in your_invite.table:
                                                            myadvisorinvite.add(l,"response","Deny")
                                                            myadvisorinvite.add(l,"response_date",datetime.now())
                                        else:
                                            print("Group already has an advisor")
                                        break
                            else:
                                print("You denied the invite")
                                for l in range(len(myadvisorinvite.table)):
                                    if myadvisorinvite.table[l]==your_invite.table[i]:
                                        myadvisorinvite.add(l,"response","Deny")
                                        myadvisorinvite.add(l,"response_date",datetime.now())
            elif option=="0":
                print("You logged out")
                break    
    elif val[1]=="member":
        while True:
            print("Options")
            print("Type 1 for viewing projects")
            print("Type 0 for logging out")
            option=input("Select options : ")
            if option=="1":
                your_proj=myproject.filter(lambda x: x["member1"]==val[0])
                if your_proj.table==[]:
                    your_proj=myproject.filter(lambda x: x["member2"]==val[0])
                print(your_proj.table)
            if option=="0":
                print("You logged out")
                break
        
    # print(myproject)
    # print(mylogin)
    # print(mymemberinvite)
# if val[1] = 'admin':
    # do admin related activities
# elif val[1] = 'advisor':
    # do advisor related activities
# elif val[1] = 'lead':
    # do lead related activities
# elif val[1] = 'member':
    # do member related activities
# elif val[1] = 'faculty':
    # do faculty related activities