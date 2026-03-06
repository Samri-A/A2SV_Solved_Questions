class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        answer = []

        steps = 1

        while len(answer) < rows*cols:
            
            # go to left
            for _ in range(steps):
                if 0 <= cStart < cols and 0 <= rStart < rows:
                   answer.append([rStart , cStart])
                
                cStart += 1
                
           
            # go to down
            for _ in range(steps):
                if 0 <= cStart < cols and 0 <= rStart < rows:
                   answer.append([rStart , cStart])
                rStart += 1
                
                
            steps+=1

            # go to right 
            for i in range(steps):
                if 0 <= cStart < cols and 0 <= rStart < rows:
                   answer.append([rStart , cStart])
                cStart -= 1
            
  

            # go to top 
            for i in range(steps):
                if 0 <= cStart < cols and 0 <= rStart < rows:
                   answer.append([rStart , cStart])
                rStart -= 1
            
            steps+=1

        return answer


            
