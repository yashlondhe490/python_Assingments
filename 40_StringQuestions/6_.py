'''
6. Check whether a string starts with a given substring.
'''
str1=input("Enter the String :")
search=input("Enter the word do u want to search at start :")
if str1.startswith(search):
    print(f"the '{search}' word found")
else:
    print(f"the '{search}' word not found")
