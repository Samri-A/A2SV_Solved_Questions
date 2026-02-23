class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Get all the column and row number of zeros
        columns = {}
        rows = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    if row not in rows:
                        rows[row] = 1

                    if col not in columns:
                        columns[col] = 1

        # make all the columns of selected value zero
        for key in columns:
            for row in range(len(matrix)):
                matrix[row][key] = 0

        # make all the rows of selected value zero
        for key in rows:
            for col in range(len(matrix[0])):
                matrix[key][col] = 0

        
