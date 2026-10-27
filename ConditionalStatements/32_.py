'''
32. Write a program to check whether a student is eligible for an exam (attendance + 
marks).
'''

attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter marks: "))

if attendance >= 75 and marks >= 40:
    print("Eligible for the exam")
else:
    print("Not eligible for the exam")