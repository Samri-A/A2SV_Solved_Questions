class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        prev =[1]

        for i in range(1 , rowIndex+1):

            new = [1] * (i+1)

            for j in range(len(prev)-1):
                new[j+1] = prev[j] + prev[j+1]

            prev = new
        
        
        return prev