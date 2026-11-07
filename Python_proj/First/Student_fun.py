
from lib import *
stud=[]
def AddStudent():
    
    while True:
                id=input("Please Enter the student ID \t\t:").strip()

                if(id==""):
                    red("Your ID is 'Blank'")
                    red("Please Enter Valid option*")
                    print()
                    continue
                elif(not id.isdigit()):
                    red("Only digits are allowed here")
                    red("Please Enter Valid option*")
                    print()
                    continue

                    # check id is present priously or not 
                found = False

                for s in stud :

                    if(s[0] == id ):    
                        found = True
                        break

                if (found):
                    print(Fore.RED+f"id- {id} is already present ")
                    red("Please Enter Valid ID*")
                    print()
                    continue
                    

                name=input("Enter the name of student\t\t:").strip().title()

                if(name==""):
                    red("Student name is 'Blank'")
                    red("Please Enter Valid option*")
                    print()

                    continue

                elif(not name.replace(" ","").isalpha()):
                    red("Only charectors are allowed here")
                    red("Please Enter Valid option*")
                    print()

                    continue

                mob=input("Please enter the Mobile number\t\t:").strip()
                if(mob==""):
                        red("Student name is 'Blank'")
                        red("Please Enter Valid option*")
                        print()

                        continue
                elif(not mob.isdigit()):
                        red("Only Digits are allowed here")
                        red("Please Enter Valid option*")
                        print()

                        continue
                if mob[0] not in "6789":
                        red("Please enter indian Origin mobile-number*")
                        red("Number is stars form [9-8-7-6]")
                        print()

                        continue
                if len(mob) != 10:
                        red("Please check the mobile number*")
                        print()

                        continue

                marks=input("Enter the marks\t\t\t\t:").strip()
                if (marks == ""):
                        red("Student marks is 'Blank'")
                        red("Please Enter Valid marks*")
                        print()
                        continue


                elif(not marks.isdigit()):
                        red("Only Digits are allowed here")
                        red("Please Enter Valid Marks*")
                        continue

                marks=int(marks)
                if(marks > 100 or marks <= 0):
                        red("Please enter the mark between 0 to 100*")
                        print()
                        continue


                city=input("Enter the City name\t\t\t:").strip().title()
                if(city==""):
                        red("City name is 'Blank'")
                        red("Please Enter Valid city name*")
                        print()
                        continue
                elif(city.isdigit()):
                       red("Digits are not allowd")
                       red("Please Enter Valid city name*")
                       print()
                       continue

                        #Store all the data in list id, name, mobile, marks, city
                stud.append([id,name,mob,marks,city])
                print()
                green("Data is inserted Succesfully")
                print()

                
                break

    

def DisplayStud():
        if(len(stud)==0):
            red("Empty Data-Base")
        else:
            print("\t{:<5}{:<20}{:<15}{:<8}{:<10}".format("id","NAME","MOBILE","MARKS","CITY"))
            print("-"*80)

            for s in stud:
                    print("\t{:<5}{:<20}{:<15}{:<8}{:<10}".format(s[0],s[1],s[2],s[3],s[4]))

            print("-"*80,"\n\n")


def SearchStud():
    while True:
        if(len(stud)==0):
            red("No Data Found")
            
        else:
            U_id=input("Enter ID to search: ")
            
            if(U_id==""):
                red("your ID is 'Blank'")
                red("Please Enter Valid ID*")
                print()

                continue

            elif(not U_id.isdigit()):
                red("Only digits are allowed here")
                red("Please Enter Valid ID*")
                print()

                continue

            found=False

            for s in stud:
                 
                 if (s[0]==U_id):
                       found=True
                       green("\n Data Found")
                       print()
                       print("-"*50,"+")
                       print("\tID       :",s[0])
                       print("\tName     :",s[1])
                       print("\tMobile   :",s[2])
                       print("\tMarks    :",s[3])
                       print("\tCity     :",s[4])
                       print("-"*50,"+","\n\n")
                       
                       

                       break
            if(not found):
                red("No reacord found.Please check the ID")
                print()
                

        break

def UpdateMarks():
      while True:
                if(len(stud)==0):
                    red("No data found in Data-Base*")
                    print()
                    break


                stud_id=input("Enter the id of student :")

                if(stud_id==""):
                    red("your ID is 'Blank'")
                    red("Please Enter Valid ID*")
                    print()

                    continue
                
                elif(not stud_id.isdigit()):
                    red("Only digits are allowed here")
                    red("Please Enter Valid ID*")
                    print()

                    continue
                
                found=False
                
                for s in stud:
                                
                    if (s[0]==stud_id):
                        found=True
                        green("Data Found")
                        print()
                        print("\t{:<5}{:<20}{:<15}{:<8}{:<10}".format("id","NAME","MOBILE","MARKS","CITY"))
                        print("-"*80)
                        print("\t{:<5}{:<20}{:<15}{:<8}{:<10}".format(s[0],s[1],s[2],s[3],s[4]))
                        print("-"*80,"\n\n")

                        break

                if(not found):
                    red("No reacord found.Please check the ID")
                    print()
                    break


                    
                op=input("You Want to change this Record's Marks (yes/no): ").lower().strip()
                match op:
                          case "yes":
                                u_mark=input("Enter the updated marks :")
                                if (u_mark == ""):
                                    red("Student marks is 'Blank'")
                                    red("Please Enter Valid marks*")
                                    print()

                                    continue
                                elif(not u_mark.isdigit()):
                                    red("Only Digits are allowed here")
                                    red("Please Enter Valid Marks*")
                                    print()
                    
                                    continue
                                else:
                                    
                                        s[3]=u_mark
                                        green("Marks changed Succesfully :")             
                                        print()
                                 
                          case "no":
                                green("Thank you*")
                                print()

                                break
                          case "":
                               red("Student marks is 'Blank'")
                               red("Please Enter Valid marks*")
                               print()

                               continue
                          case _:
                                red("plese enter given option (yes/no)*")
                                print()

                                continue
                      
                break
def DeleteStud():
        while True:    
            if(len(stud)==0):
                red("No data found in Data-Base*")
                print()
                break

      
            del_id=input("Enter the id of student :")
            

      
            if(del_id==""):
                red("your ID is 'Blank'")
                red("Please Enter Valid ID*")
                print()

                continue
                      
            elif(not del_id.isdigit()):
                  red("Only digits are allowed here")
                  red("Please Enter Valid ID*")
                  print()
                
                  continue
            
            found=False
            for s in stud:
                  if (s[0]==del_id):
                        found=True
                        green(" Data Found")
                        print()
                        print("\t{:<5}{:<20}{:<15}{:<8}{:<10}".format("id","NAME","MOBILE","MARKS","CITY"))
                        print("-"*80)
                        print("\t{:<5}{:<20}{:<15}{:<8}{:<10}".format(s[0],s[1],s[2],s[3],s[4]))
                        print("-"*80,"\n\n")
                        print()

                        break

            if(not found):
                  red("No record found. Please check the id*")
                  print()
            
            op=input("Do u really want to delete this data (yas/no) :").strip().lower()
            if(op=="yes"):
                stud.remove(s)
                green("Data deleted successfully")
            elif(op=="no"):
                  green("Thank you*")
                  print()
            else:
                  red("plese enter given option (yes/no)*")
                  print()
                  break

            break

def ExitApp():
        green("Thanks for using our App. Visit again")
    
