#To check whether the given string is a pangram:
a='abcdefghijklmnopqrstuvwxyz'
b=input("enter the string")
count=0
for i in a:
    if i in b:
        count+=1
if(count==26):
    print('Yes!It is a pangram')
else:
    print('No!It is not a pangram')
