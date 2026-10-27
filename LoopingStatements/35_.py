'''
35. Print multiplication tables from 1 to 5.
'''

table=1
while(table<=5):
    num=1

    while(num<=10):
        print(table," * ",num,"=",table*num)
        num+=1 
    print("--------------------------------")
    table+=1