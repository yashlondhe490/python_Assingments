'''
36. Find sum of numbers entered by user until 0 is entered.

'''
num=1

total = 0

while (True):
    num = int(input("Enter the number: "))
    if num== 0:
        break
    total += num

print("Sum is", total)