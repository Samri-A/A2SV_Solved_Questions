class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        track_seen = {}
        answer = []
        top = 0
        left = 0


        bottom = len(matrix)
        right = len(matrix[0])

        while left < right and top < bottom:

            # Go through top
            for i in range(left , right):
                answer.append(matrix[top][i])
            
            top+=1
    
             # Go through right
            for i in range(top , bottom):
                answer.append(matrix[i][right-1])
            right-=1


            #  Break before going inward if it reached
            if not (left < right and top < bottom):
                break
            

            #  Go through bottom
            for i in range(right-1, left-1, -1):
                answer.append(matrix[bottom-1][i])
    
            bottom -= 1

             # Go through the left
            for i in range( bottom-1 , top-1 , -1):
                answer.append(matrix[i][left])

            left+=1
        return answer
