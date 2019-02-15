n=int(input())
sr=input()
li=[]
for i in sr:
    if i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
        continue
    li.append(i)
c="".join(reversed(li))
print(c)    
    

    
