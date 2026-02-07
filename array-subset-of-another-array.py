#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a.sort()
        b.sort()
        if len(b) > len(a):
            return False
            
        pointer_a = 0
        pointer_b = 0
        while pointer_b < len(b):
           if a[pointer_a] == b[pointer_b]:
                    pointer_a += 1
                    pointer_b += 1
            
           elif a[pointer_a] > b[pointer_b]:
                return False
           else:
                pointer_a += 1
                
        
        return True
    
    
    
    
