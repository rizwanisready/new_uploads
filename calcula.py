product = 100

def option():
    a = int
    while a is int:
        e = int(input("Option 1 for Sale | Option 2 for Sale Return: "))
        if e == 1:
            sale()
        elif e == 2:
            sale_return()
def sale():
    global product
    quantity = int(input("Enter the Quantity:- "))
    product = product - quantity
    print(product)
    
def sale_return():
    global product
    quantity = int(input("Enter the Quantity:- "))
    product = product + quantity
    print(product)

option()  
