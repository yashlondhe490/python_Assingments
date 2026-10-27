'''
26. Write a program to check month names based on month number.
'''
num = int(input("Enter the num of mounths: "))
match (num):
    case 1:
        print("January")
    case 2:
        print("february")
    case 3:
            print("march")
    case 4:
            print("april")    
    case 5:
            print("MAy")
    case 6:
            print("jun")
    case 7:
            print("july")
    case 8:
              print("August")
    case 8:
                  print("saptember")
    case 8:
                  print("Auctober")
    case 8:
                  print("november")
    case 8:
                  print("december")
    case _:
                  print("invalid day")
              