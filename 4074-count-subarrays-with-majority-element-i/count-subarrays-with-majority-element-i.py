class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pre = [0] * (n + 1)

        for i in  range(n):
            pre[i+1] = pre[i] +( 1 if nums[i] == target else -1)
        

        ans = 0
        for l in range(n):
            for r in range(l , n):
                if pre[r+1] - pre[l] > 0:
                    ans += 1
        print(pre)

        return ans