from collections import OrderedDict
def r(s1):
  return "".join(OrderedDict.fromkeys(s1))
s1=input()
print(r(s1))
