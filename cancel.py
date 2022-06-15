from copy import copy


alist = ["mango", "banana", "apple", "watermelon", "grapes"]
customer = []
def intro(start):
    print("Ready for the game..??")
    start = int(input("Click 1 to continue: "))
    while start == 1:
        print("Click 5 for Booking | 6 for Cancel????")
        print(alist)
        print(customer)
        proceed = int(input("Enter the keyword:- "))
        try:
            if proceed == 5:
                booking()
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
def booking():
    print('''
    To purchase please enter below keyword
1 for mango
2 for banana
3 for apple
4 for watermelon
5 for grapes''')
    book = int(input("Enter the desired keyword: "))
    if book == 1:
        alist.remove('mango')
        customer.append('mango')
        print(f"Stock available {alist}")
        print(f"You have purchased {customer}")
    elif book == 2:
        alist.remove('banana')
        customer.append("banana")
        print(f"Stock available {alist}")
        print(f"You have purchased {customer}")
    elif book == 3:
        alist.remove('apple')
        customer.append("apple")
        print(f"Stock available {alist}")
        print(f"You have purchased {customer}")
    elif book == 4:
        alist.remove('watermelon')
        customer.append("watermelon")
        print(f"Stock available {alist}")
        print(f"You have purchased {customer}")
    elif book == 5:
        alist.remove('grapes')
        customer.append("grapes")
        print(f"Stock available {alist}")
        print(f"You have purchased {customer}")
def cancel_booking():
    print('''
    To cancel your purchase please enter below keyword
6 for mango
7 for banana
8 for apple
9 for watermelon
10 for grapes''')
    cancel = int(input("Enter the desired keyword: "))
    try:
        if cancel == 6 :
            customer.remove("mango")
            alist.append('mango')
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif cancel == 7:
            customer.remove("banana")
            alist.append('banana')
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif cancel == 8:
            customer.remove("apple")
            alist.append('apple')
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif cancel == 9:
            customer.remove("watermelon")
            alist.append('watermelon')
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif cancel == 10:
            customer.remove("grapes")
            alist.append('grapes')
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        else:
            print("Please enter correct keyword")
    except:
        print(f"Not purchased the given fruit {cancel}")
intro(start=1)