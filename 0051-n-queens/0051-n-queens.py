class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        diagonal = [0] * (2*n - 1 )
        # if (col + currentcol ) == row 
        anti_diagonal = [0] * (2*n - 1 ) 
        # if (col -  currentcol ) == row 

        path = []
        result = []

        column_filled = set()
        row = 0

        
        def place_queens(row):
            

            if row  == n:
                result.append(path.copy())
                return

 

            for col in range(n):

                if col in column_filled or  diagonal[row - col + (n-1)]  or anti_diagonal[row + col]:
                    continue 

                expression = ['.'] * n
                expression[col] = 'Q'
                expression_s = ''.join(expression)
                path.append(expression_s)
                column_filled.add(col)

                diagonal[row - col + (n-1)] = 1
                anti_diagonal[row + col] = 1

                place_queens(row + 1)


                column_filled.remove(col)
                diagonal[row - col + (n-1)] = 0
                anti_diagonal[row + col] = 0

                path.pop()

            

        place_queens(row)

        return result



