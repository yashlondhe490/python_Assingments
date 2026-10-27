'''
33. Write a program to check whether a person can apply for a loan.
'''

age = int(input("Enter your age: "))
income = int(input("Enter your monthly income (Rs): "))
credit_score = int(input("Enter your credit score (300-900): "))

if age < 21 or age > 60:
    print("Not eligible: age must be between 21 and 60")
elif income < 25000:
    print("Not eligible: monthly income must be at least 25000 Rs")
elif credit_score < 700:
    print("Not eligible: credit score must be at least 700")
else:
    print("Congratulations! You can apply for the loan")