lipstick = 100
bucket = 0
cust_cost = int
total_expense = 0

def sale():
    global lipstick
    global bucket
    global cust_cost
    global total_expense
    quantity = int(input("Enter the Quantity:- "))
    price = 120
    if quantity <= lipstick:

        lipstick = lipstick - quantity
        bucket = bucket + quantity
        cust_cost = quantity * price
        total_expense = total_expense + cust_cost
        print(f"Available Lipstick in stock is {lipstick}.")
        print(f"You have purchased {bucket} of Lipstick")
        print(f"The cost for your purchase is {cust_cost}")
        print(f"You have spent till now {total_expense} rupees.")


def sale_return():
    global lipstick
    global bucket
    global cust_cost
    global total_expense
    quantity = int(input("Enter the Quantity:- "))
    return_price = 100
    if quantity <= bucket:

        bucket = bucket - quantity
        lipstick = lipstick + quantity
        cust_cost = quantity * return_price
        total_expense = total_expense - cust_cost
        print(f"Available Lipstick in stock is {lipstick}.")
        print(f"You have purchased {bucket} number of Lipstick")
        print(f"The return cost of your purchase is {cust_cost} which is 20/- refund deduction")
        print(f"You have spent till now {total_expense} rupees.")


def option():
    print("Welcome to Sadiqa Beauty Shop...!!!")
    print(f"Available lipstick in stock is {lipstick}")
    a = int
    while a is int:
        e = int(input("Option 1 for Purchase | Option 2 for Purchase Return: "))
        if e == 1:
            sale()
        elif e == 2:
            sale_return()
option()