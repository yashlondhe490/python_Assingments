'''
Develop a small electricity billing program for a household. The electricity board
charges different rates according to the number of units consumed.
'''
from colorama import Fore,Back,Style,init
init(autoreset=True)
print("\n \n \n ")
print(Fore.YELLOW+"----------Smart-Electricity-Bill-Calculator--------------\n\n")


name = input("Enter your name: ")
unit = int(input("Enter the Electricity Units: "))
charge = 0 
serviceCharge = 150
if(unit <= 0):
    print(Fore.RED+"Envalid units please inter valid units ")
    exit(1)

elif(unit <= 100):
    charge=unit*3
elif(unit <= 200):
    charge=(100*3)+(unit-100)*5
else:
    charge=(100*3)+(100*5)+(unit-200)*7
 


finalBill = charge + serviceCharge
print("------------------------------------------\n")
print(Fore.GREEN+"Name of the customer is: ",name)
print(Fore.GREEN+"Units consumed: ",unit)
print(Fore.GREEN+"Energy charge: ",charge)
print(Fore.GREEN+"Service Charge is: ",serviceCharge)
print(Fore.GREEN+"Final bill :",finalBill)


if(finalBill > 5000):
    print(Fore.RED+"High Usage Bill\n\n\n\n")