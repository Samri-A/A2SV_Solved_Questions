class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l_row = 0
        r_row = len(matrix) - 1
        while l_row <= r_row:

            mid = (r_row + l_row)//2

            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            elif matrix[mid][0] < target < matrix[mid][-1]:
                l_col = 0
                r_col = len(matrix[mid]) - 1

                while l_col <= r_col:
                    col_mid = (l_col + r_col) // 2

                    if matrix[mid][col_mid] == target:
                        return True
                    elif matrix[mid][col_mid] < target:
                        l_col = col_mid + 1
                    else:
                        r_col = col_mid - 1

                    # print(col_mid)
                
                break

                    
                

            elif  matrix[mid][-1] < target:
                l_row = mid + 1
            else:
                r_row = mid - 1 

            
            

        return False