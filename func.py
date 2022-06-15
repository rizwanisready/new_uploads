alist = ["mango", "banana", "apple", "watermelon", "grapes"]
customer = []
def intro(start):
    print("Ready for the game..??")
    print("Click 1 to continue")
    start = int(input("Enter 1 for enter into the market"))
    while start == 1:
        booking_cancel(game=1)
    else:
        print("Enter correct keyword")
        intro(start=1)
def booking_cancel(game):
    print('''
1 for mango
2 for banana
3 for apple
4 for watermelon
5 for grapes''')
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
intro(start=1)