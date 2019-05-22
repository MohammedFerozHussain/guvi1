n=int(input())
n1=n%10
s=0
for i in range(1,len(str(n))+1):
    f=i**n1
    s+=f
print(s)    
