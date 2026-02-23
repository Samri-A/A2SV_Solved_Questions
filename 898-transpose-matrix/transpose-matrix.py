class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        pointer_row = 0
        pointer_column = 0
        row , column = len(matrix) , len(matrix[0])
        transpose = [[0] * row for _ in range(column)]
        print(transpose)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                transpose[c][r] = matrix[r][c]

        return transpose

        