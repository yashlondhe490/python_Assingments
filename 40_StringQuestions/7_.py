'''
7. Check whether a string ends with a given substring.
'''
str1=input("Enter the String :")
search=input("Enter the word do u want to search at end :")
if str1.endswith(search):
    print(f"the '{search}' word found")
else:
    print(f"the '{search}' word not found")
