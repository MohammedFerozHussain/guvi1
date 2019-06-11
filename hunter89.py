from collections import OrderedDict
def remove_duplicate(s):
  return "".join(OrderedDict.fromkeys(s))
s=input()
c=s[::-1]
print(remove_duplicate(c))

