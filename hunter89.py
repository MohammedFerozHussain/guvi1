from collections import OrderedDict
def remove_duplicate(s1):
  return "".join(OrderedDict.fromkeys(s1))
s1=input()
c=s1[::-1]
print(remove_duplicate(c))

