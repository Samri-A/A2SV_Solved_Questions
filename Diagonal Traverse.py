class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        col = len(mat[0])
        row = len(mat)

        answer = []
        going_up = True

        current_row = 0
        current_col = 0

        while len(answer) < col * row:
            
            if going_up:
                while current_row >= 0  and current_col < col:
                    answer.append(mat[current_row][current_col])
                    current_row -=1
                    current_col += 1

                if current_col == col:
                    current_col -=1
                    current_row +=2
                else:
                    current_row +=1


                going_up=False
            else:
                while current_row < row  and current_col >= 0:
                   answer.append(mat[current_row][current_col])
                   current_row +=1
                   current_col -= 1

                if current_row == row:
                    current_col +=2
                    current_row -=1
                else:
                    current_col +=1
                going_up = True

        return answer
