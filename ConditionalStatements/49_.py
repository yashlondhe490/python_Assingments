'''
49. Write a program to print result status using match case.
'''

marks = int(input("Enter marks (0-100): "))

match marks:
    case m if m >= 75:
        print("Pass with Distinction")
    case m if m >= 35:
        print("Pass")
    case m if m >= 0:
        print("Fail")
    case _:
        print("Invalid marks")