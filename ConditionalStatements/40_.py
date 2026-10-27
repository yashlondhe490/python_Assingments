'''
40. Write a program to check whether a password is valid using nested if.
'''
login="yash"
passd=123
userlog=input("Enter the login-id :")
userpass=int(input("Enter the passward : "))

if (login==userlog):
    if(passd==userpass):
        print("Login succesfully");

else:
    print("envalid loginid")