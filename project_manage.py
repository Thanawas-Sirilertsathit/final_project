# import database module
import database
import random
# start by adding the admin related code

# create an object to read an input csv file, persons.csv

# create a 'persons' table
table=database.Table("persons",database.persons)
data=database.DB()
data.insert(table)
myperson=data.search("persons")
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
    myperson.add(i,"password",password)
print(myperson)
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
