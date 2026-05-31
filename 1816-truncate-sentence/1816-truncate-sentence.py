class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split()

        ans = f"{arr[0]}"

        for i in range(1, k):
            ans +=  " "  + arr[i] 

        # print(arr)

        return ans