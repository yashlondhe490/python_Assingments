'''
41. Write a program to print weekday name using match case.
'''
num = int(input("Enter the number : "))
match (num):
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
            print("Tuesday")
    case 4:
            print("Wednesday")    
    case 5:
            print("Thusday")
    case 6:
            print("Friday")
    case 7:
            print("Saturday")
    case _:
              print("invalid day")