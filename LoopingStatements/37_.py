'''
37. Print numbers until user enters a negative number.
'''
total = 0

while True:
    num = int(input("Enter the number: "))
    if num < 0:
        break
    total += num

print("Sum is", total)