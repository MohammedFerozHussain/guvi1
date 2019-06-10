x=int(input())
lis=[]
for i in range(2,x+1):
    if(i>1):
      if x==2:
        print("0")
        break
      else:  
        
        for v in range(2,i):
            if(i%v==0):
               break
        else:
            lis.append(i)
print(*lis)
            

          
       
