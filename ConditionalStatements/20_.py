'''
20. Write a program to check ticket price based on age.
'''
age=int(input("Enter your age: "))
print("-----------------------")
print("1.Pune-Gova-Pune")
print("2.Pune-Mumbai-Pune")
print("3.Pune-Channai-Pune")
print("4.Pune-Banglor-Pune")
print()
opt=int(input("Enter your option to buy tickets : "))
match opt:
    case 1:
        price=120
        print("Actual Ticket price is =",price,"Rs")
        if(age>60):
            price/=2;
            print("-----------------")
            print("50%= ",price,"Rs")
        else:
            print("-----------------")
            print("Your price is ",price)
    case 2:
            price=3000
            print("Actual Ticket price is =",price,"Rs")
            if(age>60):
                price/=2;
                print("-----------------")
                print("50%= ",price,"Rs")
            else:
                print("-----------------")
                print("Your price is ",price)
    case 3:
                price=5300
                print("Actual Ticket price is =",price,"Rs")
                if(age>60):
                    price/=2;
                    print("-----------------")
                    print("50%= ",price,"Rs")
                else:
                    print("-----------------")
                    print("Your price is ",price)            
    case 4:
                price=5300
                print("Actual Ticket price is =",price,"Rs")
                if(age>60):
                    price/=2;
                    print("-----------------")
                    print("50%= ",price,"Rs")
                else:
                    print("-----------------")
                    print("Your price is ",price)
    case _:
            print("invalid option: ")