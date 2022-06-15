alist = ['mango', 'banana', 'apple', 'watermelon', 'grapes']
customer = []

print("Ready for the game..??")
print("Click 1 to continue")
game = int(input("Enter the keyword.: "))


while game == 1 :
    print("to buy fruits click 1:mango, 2:banana, 3:apple, 4:watermelon, 5:grapes")
    print("to return fruits click 6:mange, 7:banana, 8:apple, 9:watermelon, 10:grapes")
    v = int(input("enter the fruit index number:- "))
    try:
        if v == 1:
            alist.remove('mango')
            customer.append('mango')
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif v == 2:
            alist.remove('banana')
            customer.append("banana")
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif v == 3:
            alist.remove('apple')
            customer.append("apple")
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif v == 4:
            alist.remove('watermelon')
            customer.append("watermelon")
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif v == 5:
            alist.remove('grapes')
            customer.append("grapes")
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif v == 6:
            alist.append('mango')
            customer.remove("mango")
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif v == 7:
            alist.append('banana')
            customer.remove("banana")
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif v == 8:
            alist.append('apple')
            customer.remove("apple")
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif v == 9:
            alist.append('watermelon')
            customer.remove("watermelon")
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        elif v == 10:
            alist.append('grapes')
            customer.remove("grapes")
            print(f"Stock available {alist}")
            print(f"You have purchased {customer}")
        else:
            print("Please enter correct keyword")
    except:
        print("Have not purchased yet to return")
        
else:
    print("Sorry Not in list")