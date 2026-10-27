'''
50. Write a program to build a simple ATM menu using a match case.
'''
balance = 10000

while True:
    print("\n---------- ATM Menu ----------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Your balance is:", balance, "Rs")
        case 2:
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print("Deposited", amount, "Rs. New balance:", balance, "Rs")
            else:
                print("Invalid amount")
        case 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Invalid amount")
            elif amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
                print("Withdrawn", amount, "Rs. New balance:", balance, "Rs")
        case 4:
            print("Thank you for using the ATM")
            break
        case _:
            print("Invalid choice, try again")

            
