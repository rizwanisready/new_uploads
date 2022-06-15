
import datetime
from nptime import nptime
booking_form = []
start_date = datetime.date(year= 2022, month=6, day=3)
end_date = datetime.date(year= 2022, month=6, day=9)

t = datetime.timedelta(days=1)
empty_list_date = []
empty_list_time = []
while start_date <= end_date:
    start_date = start_date + t
    
    empty_list_date.append(str(start_date))
a = empty_list_date



new_start_time = nptime(8, 0)
s = datetime.timedelta(hours=1)
end_time = datetime.time(hour=14, minute=30, second=0)
while new_start_time < end_time:
        
    new_start_time = new_start_time + s
    empty_list_time.append(str(new_start_time))
v = empty_list_time

def select_doctor():
    
    print("ID : 1 : Dr.Sohan Shirke | Mobile No: 54321")
    print("MBBS, MD Specialist")
    
    
    doctor = {
        1 : "Sohan Shirke | Mobile No: 54321",
        }
    a = int(input("Enter keyword 1 to proceed: "))
    booking_form.append(doctor[a])
    if a == 1 :
        select_date()
    else:
        print("Choose correct option..")


def select_date():
    print("Which date you would like to book?")
    print("1 : 2022-06-04")
    print("2 : 2022-06-05")
    print("3 : 2022-06-06")
    print("4 : 2022-06-07")
    print("5 : 2022-06-08")
    print("6 : 2022-06-09")
    print("7 : 2022-06-10")
    
    
    b = int(input("Enter the day: "))
    booking_form.append(a[b])
    if 
    if b == 1 or b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7:
        select_time()
    else:
        print("Choose a valid key word")

def select_time():
    print("Below are the time slots available for booking: ")
    print("1 : 09.00 - 10.00")
    print("2 : 10.00 - 11.00")
    print("3 : 11.00 - 12.00")
    print("4 : 12.00 - 13.00")
    print("5 : 13.00 - 14.00")
    print("6 : 14.00 - 15.00")
    print("7 : 15.00 - 16.00")   
    
    
    c = int(input("Select the time slot: "))
    booking_form.append(v[c])
    v.pop(c)
    if c == 1 or c == 2 or c == 3 or c == 4 or c == 5:
        print("Your appointment has been booked successfuly")
        print(f"Doctor Name: {booking_form[0]}")
        
        print(f"Booking done for {booking_form[1]}")
        print(f"Timing: {booking_form[2]}")
        print("In case of any changes, inform the below number at least 48 hours before the booking time.")
        print("Contact Number: 06543365")
        print(booking_form)
    else:
        print("Choose a valid keyword..")

print("Welcome to Dr.Sohan Shirke Hospital")
print(f"Available dates are {a}")
print(f"Available appointments are {v}")

def cancel_booking():
    pass

def intro(start):
    print("We Care More!!")
    start = int(input("Click 1 to continue: "))
    while start == 1:
        print("Click 5 for Booking | 6 for Cancel????")
        print(a)
        print(v)
        proceed = int(input("Enter the keyword:- "))
        try:
            if proceed == 5:
                select_doctor()
            elif proceed == 6:
                cancel_booking()
            else:
                intro(start=1)
        except:
            print("Enter correct keyword")
            intro(start=1)
    else:
        print("Enter correct keyword")
        intro(start=1)

intro(start=1)
