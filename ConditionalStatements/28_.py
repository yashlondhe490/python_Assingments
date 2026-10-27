'''
28. Write a program to calculate discounts based on total shopping amount.
'''
amt = int(input("Enter the Total amount of shopping : "))

if amt >= 8000:
    discount_per = 20
elif amt >= 4000:
    discount_per = 15
elif amt >= 2000:
    discount_per = 10
else:
    discount_per = 0

discount = amt * discount_per / 100
totalPrice = amt - discount

print(discount_per, "% off price is =", totalPrice)