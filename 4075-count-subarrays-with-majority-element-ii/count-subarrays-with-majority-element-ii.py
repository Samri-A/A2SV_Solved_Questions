from bisect import bisect_left
class Fenwick:
    def __init__(self ,n):
        self.n = n
        self.bit = [0] * (n+1)

    def query(self , i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i

        return res
    
    def update(self , i , delta):

        while i <= self.n:
            self.bit[i] += delta
            i += i & -i


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        arr = [0] * (n+1)

        for i in range(n):

            arr[i+1] = arr[i] + (1 if nums[i] == target else -1)

        pre = sorted(set(arr))

        



        ans = 0
        bit = Fenwick(len(pre))

        for x in arr:
            idx = bisect_left(pre,x) + 1
            ans += bit.query(idx - 1)
            bit.update(idx , 1)


        return ans