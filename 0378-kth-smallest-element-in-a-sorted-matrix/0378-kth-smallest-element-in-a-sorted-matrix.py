import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        row = len(matrix)
        col = len(matrix[0])


        k_smalls = []
        heapq.heapify(k_smalls)

        for i in range(row):
            for j in range(col):
                heapq.heappush(k_smalls , matrix[i][j])
                
        
        while len(k_smalls) > (row * col - k + 1):
            heapq.heappop(k_smalls)
        
        print(k_smalls)

        return heapq.heappop(k_smalls)