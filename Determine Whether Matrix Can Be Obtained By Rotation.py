class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        if len(mat) != len(mat[0]) or  len(target) != len(target[0]) or len(target) != len(mat) :
            return False

        n = len(mat)
        m = len(mat[0])

        for _ in range(4):

            # Transpose
            for i in range(n):
                for j in range(i, m):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            # Reverse each row
            for row in mat:
                row.reverse()
            
            if mat == target:
                return True

        return False

        

        
