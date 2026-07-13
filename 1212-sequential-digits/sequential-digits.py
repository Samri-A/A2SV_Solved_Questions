class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        num = "123456789"

        l = len(str(low))

        ans = []


        for i in range(len(num)):
            for j in range(i+l , len(num)+1):
                val = int(num[i:j])

                if low <= val <= high:
                    ans.append(val)
                


        ans.sort()
        return ans