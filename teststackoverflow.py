choise = ""
exitString = "exit"
list = []
while choise != "exit":
    print("Welcome to my program, choose option what you want, 1 to add some values, 2 to add strings to list, 3 to exit ")
    try:
        choise = input("do you see me?")
        if choise == 1:
            print("provide number 1: ")
            firstNumber = input()
            print("provide number 2: ")
            secondNumber = input()
            sum = firstNumber + secondNumber
            print("sum is: " + str(sum))
        elif choise == 2:
            print("please provide string to add: ")
            stringToAdd = input()
            list.append(stringToAdd)
        elif choise == 3:
            break
    except TypeError:
        print("wrong number.")