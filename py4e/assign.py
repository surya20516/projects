import re
handle=open('assignment.txt')
sum=0
for line in handle:
    num=re.findall('[0-9]+',line)
    for i in num:
        value=int(i)
        sum=sum+value
print(sum)        
 
