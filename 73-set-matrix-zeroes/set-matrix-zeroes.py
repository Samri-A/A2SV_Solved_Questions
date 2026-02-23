class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        columns = {}
        rows = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    if row not in rows:
                        rows[row] = 1

                    if col not in columns:
                        columns[col] = 1

        for key in columns:
            for row in range(len(matrix)):
                matrix[row][key] = 0

        for key in rows:
            for col in range(len(matrix[0])):
                matrix[key][col] = 0

        print( rows , columns )

