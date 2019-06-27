def a(l, n1): 
    l.sort()  
    i = 0
    j = n1-1
      
    while (i < j):
        print(l[j], end =" ") 
        j-= 1
        print(l[i], end =" ") 
        i+= 1
    if (n1 % 2 != 0): 
        print(l[i]) 
n1=int(input())        
l=list(map(int,input().split())) 
a(l, n1)      
