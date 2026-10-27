'''
32. Calculate power of a number without using pow().
'''

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = 1
for i in range(exp):
    result *= base

print(result)
