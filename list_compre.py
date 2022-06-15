from gyp import empty_list_time
from datetime import datetime
print("welcome to the Aafiya Clinic")
form = []
yne = []
lstjohnson = []
harry = []
potter = []
indira = []
prabha = []

lstdwayne = yne.append(empty_list_time)

def cust_details():
   
    fname = input("Enter your First name:- ")
    lname = input("Enter your Last name:- ")
    age = int(input("Enter your Age:- "))
    sex = input("Enter your Sex:- ")
    

def speciality():
    print("Press 1 for General Doctor")      
    print("Press 2 for Dentist")
    print("Press 3 for Gynocologist")
    a = int(input("Enter the specialist doctor keyword:- "))
    if a == 1:
        general()
    elif a == 2:
        dentist()
    elif a == 3:
        gynocologist()
    else:
        print("specialist")

def general():
    print("We have 2 genral practitioner, 1. Dr. Dwayne | 2. Dr. Johnson")
    choose = int(input("1. Dr. Dwayne | 2. Dr. Johnson"))
    if choose == 1:
        
        dwayne()
    elif choose == 2:
        lstjohnson.append(empty_list_time)
        johnson()

def dwayne():
    time_slot = int(input("Enter time slot: "))
    if time_slot == 1:
        lstdwayne.remove('08:30:00')
        form.append('08:30:00')
        print(lstdwayne)
        print(form)
        
        

    def johnson():
        time_slot = int(input("Enter time slot: "))
        if time_slot == 2:
            lstjohnson.remove('09:00:00')
            form.append('09:00:00')
            print(lstjohnson)
            print(form)

def dentist():
    print("We have 2 dentist, 1. Dr. Harry | 2. Dr. Potter")
    choose = int(input("1. Dr. Harry | 2. Dr. Potter"))
    if choose == 1:
        harry()
    elif choose == 2:
        potter()

        def harry():
            pass

        def potter():
            pass

def gynocologist():
    print("We have 2 gynocologist, 1. Dr. Indira | 2  Dr. Prabha") 
    choose = int(input("1. Dr. Indira | 2. Dr. Prabha"))
    if choose == 1:
        indira()
    elif choose == 2:
        prabha()

    def indira():
        cust_details()

    def prabha():
        cust_details()
print(list(lstdwayne))