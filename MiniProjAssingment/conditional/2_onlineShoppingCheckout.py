'''
Statement: Create a checkout program for an online shopping website. The discount depends on
the purchase amount, and premium customers receive an additional benefit.
'''
from colorama import Fore,init
init(autoreset=True)

print("\n\n\n\n\n")
print(Fore.GREEN+"----------Welcome-To-Online-Shoping-Checkout--------------")
print("\n\n")

name = input("Enter your name: ")
paidAmt = int(input("Enter the Purchase Amount: "))
typeof=input("regular='R' or premium='P': ").lower()

if(typeof!='r' and typeof!='p'):
    print(Fore.RED+"Enter R or P only")
    exit(1)

total=0
if(paidAmt<=0):
    print(Fore.RED+"Please enter a valid amount")
    exit(1)

elif(paidAmt >= 5000):
    discount=paidAmt*20/100
    total=paidAmt-discount

elif(paidAmt >= 3000 and paidAmt < 5000):
    discount=paidAmt*10/100
    total=paidAmt-discount

elif(paidAmt >= 1000 and paidAmt < 3000):
    discount=paidAmt*5/100
    total=paidAmt-discount

else:
    total=paidAmt

 
final=total
if(typeof=='p'):
    additional=total*5/100
    final=total-additional

 
if(final>=2000):
    delivery=0
else:
    delivery=100

totalDiscount=paidAmt-final
payable=final+delivery

print("------------------------------------------\n")
print(Fore.GREEN+"Customer name: ",name)
print(Fore.GREEN+"Discount amount: ",totalDiscount)
print(Fore.GREEN+"Delivery charge: ",delivery)
print(Fore.GREEN+"Final payable amount: ",payable)