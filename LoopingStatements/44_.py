'''
44. Print alternate characters of a string.

'''
st=input("Enter the String : ")
i=0
while(i < len(st)):
     if(i%2==0):
          print(st[i],end=" ")
     i+=1