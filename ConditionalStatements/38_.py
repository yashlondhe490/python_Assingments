'''
38. Write a program to check whether a student passed all subjects.
'''
maths = int(input("Enter maths marks: "))
science = int(input("Enter science marks: "))
english = int(input("Enter english marks: "))

if maths >= 35 and science >= 35 and english >= 35:
    print("Student passed all subjects")
else:
    print("Student did not pass all subjects")