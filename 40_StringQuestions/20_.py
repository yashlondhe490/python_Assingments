'''
20. Remove all occurrences of a given character from a string.

'''

str1 = input("Enter a string: ")
ch = input("Enter the character to remove: ")

result = str1.replace(ch, "")
print("Result:", result)