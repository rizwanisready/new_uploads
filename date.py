import datetime
from pickle import TRUE
booking_form = []
day1_start_date = datetime.datetime(year=2022,month=6,day=5,hour=8,minute=00)
day1_end_date = datetime.datetime(year=2022,month=6,day=5,hour=15,minute=00)
gap = datetime.timedelta(hours=1)
day1_slots = []
day2_slots = []
day3_slots = []
while day1_start_date < day1_end_date:
    
    day1_start_date = day1_start_date + gap
    day1_slots.append(str(day1_start_date))
    
day2_start_date = datetime.datetime(year=2022,month=6,day=6,hour=8,minute=00)
day2_end_date = datetime.datetime(year=2022,month=6,day=6,hour=15,minute=00)
gap = datetime.timedelta(hours=1)
day2_slots = []
while day2_start_date < day2_end_date:
    
    day2_start_date = day2_start_date + gap
    day2_slots.append(str(day2_start_date))

day3_start_date = datetime.datetime(year=2022,month=6,day=7,hour=8,minute=00)
day3_end_date = datetime.datetime(year=2022,month=6,day=7,hour=15,minute=00)
gap = datetime.timedelta(hours=1)
day3_slots = []
while day3_start_date < day3_end_date:
    
    day3_start_date = day3_start_date + gap
    day3_slots.append(str(day3_start_date))

def select_date():
    print("Which date you would like to book?")
    print("1 : 2022-06-05")
    print("2 : 2022-06-06")
    print("3 : 2022-06-07")
        
    
    b = int(input("Enter the day: "))
    
    
    if b == 1: 
        day1_select_time()
    elif b == 2:
        day2_select_time()
    elif b == 3:
        day3_select_time()
    else:
        print("Choose a valid key word")

def day2_select_time():
    print("Below are the time slots available for booking: ")
    print("1 : 09.00 - 10.00")
    print("2 : 10.00 - 11.00")
    print("3 : 11.00 - 12.00")
    print("4 : 12.00 - 13.00")
    print("5 : 13.00 - 14.00")
    print("6 : 14.00 - 15.00")
    print("7 : 15.00 - 16.00")   
    
    
    c = int(input("Select the time slot: "))
    booking_form.append(day2_slots[c])
    day2_slots.pop(c)
    if c == 1 or c == 2 or c == 3 or c == 4 or c == 5:
        print(booking_form)
        print(day2_slots)
    else:
        print("Choose a valid keyword..")


def day3_select_time():
    print("Below are the time slots available for booking: ")
    print("1 : 09.00 - 10.00")
    print("2 : 10.00 - 11.00")
    print("3 : 11.00 - 12.00")
    print("4 : 12.00 - 13.00")
    print("5 : 13.00 - 14.00")
    print("6 : 14.00 - 15.00")
    print("7 : 15.00 - 16.00")   
    
    
    c = int(input("Select the time slot: "))
    booking_form.append(day3_slots[c])
    day3_slots.pop(c)
    if c == 1 or c == 2 or c == 3 or c == 4 or c == 5:
        print(booking_form)
        print(day3_slots)
    else:
        print("Choose a valid keyword..")


def day1_select_time():
    print("Below are the time slots available for booking: ")
    print("1 : 09.00 - 10.00")
    print("2 : 10.00 - 11.00")
    print("3 : 11.00 - 12.00")
    print("4 : 12.00 - 13.00")
    print("5 : 13.00 - 14.00")
    print("6 : 14.00 - 15.00")
    print("7 : 15.00 - 16.00")   
    
    
    c = int(input("Select the time slot: "))
    booking_form.append(day1_slots[c])
    day1_slots.pop(c)
    if c == 1 or c == 2 or c == 3 or c == 4 or c == 5:
        print(booking_form)
        print(day1_slots)
    else:
        print("Choose a valid keyword..")

def intro(start):
    print("We Care More!!")
    start = int(input("Click 1 to continue: "))
    while start == 1:
        print("Click 5 for Booking | 6 for Cancel????")
        print(booking_form)
        print(f"Availability for 5 June is {day1_slots}")
        print(f"Availability for 6 June is {day2_slots}")
        print(f"Availability for 7 June is {day3_slots}")
        proceed = int(input("Enter the keyword:- "))
        try:
            if proceed == 5:
                select_date()
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

def cancel_booking():
    pass
