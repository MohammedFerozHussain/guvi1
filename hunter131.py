def a(l, n): 
    l.sort()  
    i = 0
    j = n-1
      
    while (i < j):
        print(l[i], end =" ") 
        i+= 1
        print(l[j], end =" ") 
        j-= 1
    if (n % 2 != 0): 
        print(l[i])  
l=list(map(int,input().split()))  
n=len(l) 
a(l, n)      
