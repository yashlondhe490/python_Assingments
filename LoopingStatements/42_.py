'''
42. Calculate sum of squares of first n numbers.
'''

endVal=int(input("Enter the nth digit : "))
i= 0
total=0
while(i<=endVal):
    total+=i*i
    i+=1
print(total)

