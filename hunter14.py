from itertools import permutations 
  
def allPermutations(str1): 
     p = permutations(str1) 
     for i in list(p): 
         print (''.join(i)) 
if __name__ == "__main__": 
    str1 =input()
    allPermutations(str1) 
        
