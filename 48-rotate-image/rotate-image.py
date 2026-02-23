class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Let have temporary maxtix to relocate the cells
        n = len(matrix)
        temp_matrix = [[0] * n  for _ in matrix[0]]
       

        # Rotate the cells to the temporary maxtix

        for row in range(len(matrix)):
            n-=1
            for col in range(len(matrix)):
                temp_matrix[col][n] = matrix[row][col]

            
        
        matrix[:] = temp_matrix
        



        