def check(string1):
    p = set(string1) 
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}: 
        print("yes") 
    else : 
        print("no") 
if __name__ == "__main__" : 
  
    string1 = input()
    check(string1) 
