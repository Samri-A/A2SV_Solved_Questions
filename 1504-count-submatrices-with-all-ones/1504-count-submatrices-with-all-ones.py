class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        arr = [0] * cols
        result = 0


        for row in range(rows):

            for col in range(cols):
                if mat[row][col]:
                    arr[col] += 1

                else:
                    arr[col] = 0
                
            
            for col in range(cols):
                minheight = arr[col]

                for k in range(col , -1 ,-1):
                    minheight = min(minheight ,arr[k] )

                    if minheight == 0:
                        break 

                    result += minheight
                    

                

            

        # print(arr)

        return result
        