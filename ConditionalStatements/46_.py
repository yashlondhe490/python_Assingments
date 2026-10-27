'''
 46. Write a program to print grade description using match case.
'''
grade = input("Enter your grade (A/B/C/D/F): ").strip().upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass, needs improvement")
    case "F":
        print("Fail, try again")
    case _:
        print("Invalid grade")