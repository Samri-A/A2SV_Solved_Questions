class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        shifted = [0] * (len(s) + 1)

        for shift in shifts:
            if shift[2] == 0: 
                shifted[shift[0] ] -=1
                shifted[shift[1] + 1] += 1
                
            else:
                shifted[shift[0] ] +=1
                shifted[shift[1] + 1] -= 1

        

        current = 0
        for j in range(len(shifted)):
            current += shifted[j]
            shifted[j] = current
        
        
        answer = ""
        for  i in range(len(s)):
            temp = (ord(s[i]) - ord('a')  + shifted[i])%26 + ord('a')
            
            answer += chr(temp)
        
        
        return answer