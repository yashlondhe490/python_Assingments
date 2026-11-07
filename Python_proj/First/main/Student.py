'''
Student Managament System
Operations
------------------
1. Add Student --> Field --> id, name, mobile, marks, city
2. Display all student
3. Search Student
4. Update marks 
5. Delete Student by using id
6. Exit
Complete the project with validations
'''
from lib import *
from Student_fun import *
init(autoreset=True)

while True:
    
    print(Fore.YELLOW+"~"*20+Fore.YELLOW+" |STUDENT MANAGEMENT SYSTEM| ",Fore.YELLOW+"~"*20,"\n")
    yellow("\t 1. Add Student")
    yellow("\t 2. Display All Student")
    yellow("\t 3. Search Student")
    yellow("\t 4. Update Marks")
    yellow("\t 5. Delete Student By Id")
    yellow("\t 6. Exit \n\n\n")

    op=input("Enter your option :")
    print("-"*80)

    if(op==""):
        red(Fore.RED+"Your Option is 'Blank'")
        red(Fore.RED+"Please Enter Valid option*")
        continue
    
    elif(not op.isdigit()):
        red("Only numbers are allowed here")
        red("Please Enter Valid option*")
        continue

    else:
        op=int(op)


    match(op):
        case 1:
            AddStudent()  
        case 2:
            DisplayStud()
        case 3:
            SearchStud()
        case 4:
            UpdateMarks()
        case 5:
            DeleteStud()
        case 6:
            ExitApp()
            break
        case _:
            red("Envalid Case Plese Enter valid case ")