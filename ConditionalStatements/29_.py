'''
29. Write a program to check blood donation eligibility based on age and weight.
'''
age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))

if age >= 18 and age <= 65 and weight >= 50:
    print("Eligible to donate blood")
else:
    print("Not eligible to donate blood")