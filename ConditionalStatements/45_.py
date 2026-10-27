# 44. Write a program to check traffic signal actions using match case.


'''
print("----------WELCOME TO HOTEL 'KSHITIJA'-----------")
print()
print()

option =int(input("1.Veg---------2.Non-veg : "))
match option:
    case 1: 
        print("----------Veg-Menue---------------")
        i=0
        price=0
        for i in range(i,True):

            print("1.poha          --------------------------- 40.Rs")
            print("2.Idli         ---------------------------  50.Rs")
            print("3.jira-Rice    ---------------------------  50.Rs")
            print("4.panir Tikka  --------------------------  110.Rs")
            print("5.shev bhaji   -----------------------------70.Rs")
            print("6.------------------EXIT-------------------------")
            
            print()
            vegOpt=int(input("Enter which item u like: "))
            if(vegOpt==1):
                price+=40
            elif(vegOpt==2):
                price+=50
            elif(vegOpt==3):
                price+=50
            elif(vegOpt==4):
                price+=50
            elif(vegOpt==5):
                price+=50 
            else:
                print("envalid option")
                break
    



                

       
    # case 2:
    #     print("----------Veg-Menue---------------")
    #     print("1.chiken 65           --------------------------- 100.Rs")
    #     print("2.chicken biryani    ---------------------------  120.Rs")
    #     print("3.matan biryani      ---------------------------  400.Rs")
    #     print("4.matan handi         --------------------------- 340.Rs")
    #     print("5.manchuriyan         -----------------------------70.Rs")
    # case 3:
    #     print("Envalid option"
'''

print("---------- Food Menu ----------")
print("1. Veg")
print("2. Non-Veg")
print("3. Drinks")
print("0. Exit")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Veg Menu: Poha, Idli, Jeera Rice, Paneer Tikka")
    case 2:
        print("Non-Veg Menu: Chicken Biryani, Egg Curry, Fish Fry")
    case 3:
        print("Drinks Menu: Tea, Coffee, Lassi, Cold Drink")
    case 0:
        print("Thank you, visit again!")
    case _:
        print("Invalid choice")