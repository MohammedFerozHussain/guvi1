x = int(input())  
s = 0  
t = x  
  
while t > 0:  
   digit = t % 10  
   s += digit ** 3  
   t //= 10  
  
if x == s:  
   print("yes")  
else:  
   print("no")  
