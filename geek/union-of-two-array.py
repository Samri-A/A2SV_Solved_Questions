class Solution:    
    def findUnion(self, a, b):
        # code here
        a.sort()
        b.sort()
        answer = []
        pointer_a = 0
        pointer_b = 0
        while pointer_a < len(a) and pointer_b < len(b):
            if a[pointer_a] < b[pointer_b]:
               answer.append(a[pointer_a])
               pointer_a+= 1
            elif a[pointer_a] == b[pointer_b]:
               answer.append(a[pointer_a])
               pointer_a+= 1
               pointer_b+=1
            else :
               answer.append(b[pointer_b])
               pointer_b+=1
        
        if pointer_a < len(a) :
           previous = pointer_a - 1
           while pointer_a < len(a):
               if a[pointer_a] != a[previous]:
                   answer.append(a[pointer_a])
                   pointer_a+= 1
                   previous+= 1
               else: pointer_a+= 1
                
                   
        if pointer_b < len(b):
           previous = pointer_b - 1
           while pointer_b < len(b):
               if b[pointer_b] != b[previous]:
                   answer.append(b[pointer_b])
                   pointer_b+= 1
                   previous+= 1
               else: pointer_b+= 1
        return answer
        
        
             
