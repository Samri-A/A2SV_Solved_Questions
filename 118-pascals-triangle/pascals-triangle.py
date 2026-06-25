class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]
        
        for i in range(2,numRows+1 ):

            prev = res[i-2]
            new = [1] * i

            for j in range(len(prev)-1):
                new[j+1] = prev[j] + prev[j+1]


            res.append(new)

        return res