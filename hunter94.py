def r(s):
    return ' '.join(i[::-1] for i in s.split(" ")) 
s=input()
print(r(s))     
