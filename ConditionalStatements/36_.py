'''
36. Write a program to check whether a person is eligible for a driving license.
'''
age = int(input("Enter age: "))
has_test = input("Passed driving test? (yes/no): ").lower()

if age >= 18:
    if has_test == "yes":
        print("Eligible for a driving license")
    else:
        print("Not eligible: driving test not passed")
else:
    print("Not eligible: age is below 18")