'''
46. Print first n multiples of a number.
'''

num = int(input("Enter the number :"))
nth = int(input("Enter nth number :"))
i = 1
while i <= nth:
    print(num * i)
    i += 1