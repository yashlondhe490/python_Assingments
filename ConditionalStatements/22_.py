'''
22. Write a program to check salary bonus based on years of service.
'''
salHike=25000
exp=int(input("Enter your experience in years (1-3): "))

if exp==1:
    salHike*=1.2;
    print(salHike)
elif(exp==2):
    salHike=salHike*2.1;
    print(salHike)
elif(exp==3):
    salHike=salHike*2.5;
    print(salHike)
else:
    print("envalid experience years: ")