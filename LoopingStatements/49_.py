'''

49. Display menu-driven program using while loop.
'''
while True:
    print("\n-----CALCULATOR-----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print()
    print("------------------------")

    option = int(input("Enter your choice: "))

    if (option < 1 or option > 4):
        print("Invalid choice, try again")
        continue
    
    if (option == 5):
        print("Program ended")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if (option == 1):
        print("Result:", a + b)


    elif (option == 2):        
        print("Result:", a - b)

    elif (option == 3):
        print("Result:", a * b)

    elif (option == 4):
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a / b)