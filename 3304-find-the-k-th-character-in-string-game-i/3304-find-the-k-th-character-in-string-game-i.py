class Solution:
    def kthCharacter(self, k: int) -> str:
        
        answer = ["a"]

        def construct_chars():
            if len(answer[0]) >= k:
                return
  
            temp = ""
            for i in range(len(answer[0])):
                
                temp += chr((ord(answer[0][i]) - ord('a') + 1 )% 26 + ord('a'))
            
            answer[0] += temp

            # print(temp)
            construct_chars()

        construct_chars()
        # print(answer)

        return answer[0][k-1]

        

