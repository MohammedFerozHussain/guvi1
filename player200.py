from collections import OrderedDict 
def r(s): 
    return "".join(OrderedDict.fromkeys(s))  
s=input()
print (r(s))
