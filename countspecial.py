s=input()
a=d=sp=0
for i in range(len(s)):
    if(s[i].isalpha()):
        a=a+1
    elif(s[i].isdigit()):
        d=d+1
    else:
        sp=sp+1
print(sp)
