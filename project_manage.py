# import database module
import database
import random
# start by adding the admin related code

# create an object to read an input csv file, persons.csv

# create a 'persons' table
login_data=[]
table=database.Table("persons",database.persons)
login_table=database.Table("login",login_data)
data=database.DB()
data.insert(table)
data.insert(login_table)
myperson=data.search("persons")
mylogin=data.search("login")
print(myperson)
for i in range(len(table.table)):
    digit1=random.randint(0,9)
    digit2=random.randint(0,9)
    digit3=random.randint(0,9)
    digit4=random.randint(0,9)
    digit1=str(digit1)
    digit2=str(digit2)
    digit3=str(digit3)
    digit4=str(digit4)
    password=digit1+digit2+digit3+digit4
    firstname=table.table[i]["fist"]
    lastname=table.table[i]["last"]
    firstcharlast=lastname[0]
    username=firstname+"."+firstcharlast
    role=table.table[i]["type"]
    if role=="student":
        initial_role="Member"
    elif role=="faculty":
        initial_role="Faculty"
    elif role=="admin":
        initial_role="Admin"
    person_id=table.table[i]["ID"]
    mylogin.table.append({"role":initial_role})
    # myperson.add(i,"role",initial_role)
    mylogin.add(i,"username",username)
    mylogin.add(i,"password",password)
    mylogin.add(i,"person_id",person_id)
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
        return(your_account.select(["role","person_id"]))
    else:
        print("Username or password is incorrect")
        return None

# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [person_id, role] if valid, otherwise returning None

# make calls to the initializing and login functions defined above

# initializing()
val = log_in()

# END part 1

# CONTINUE to part 2 (to be done for the next due date)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

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