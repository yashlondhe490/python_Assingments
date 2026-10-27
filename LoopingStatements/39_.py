'''
39. Count total words in a string.
'''
word=input("Enter the para :")
cnt=0
i=0
while(i< len(word)):

    if(word[i]==" "):
        cnt+=1
    i+=1
print("Total spaces are ",cnt)