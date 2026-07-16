import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        mx = nums[0]
        prefixGcd = []
        for i in range(len(nums)):
            mx = max(mx , nums[i])
            prefixGcd.append(math.gcd(mx , nums[i]))

        print(prefixGcd)

        prefixGcd.sort()

        left = 0
        right = len(prefixGcd) - 1

        ans = 0

        while left < right:

            gcp = math.gcd(prefixGcd[left] , prefixGcd[right])

            ans += gcp
            left += 1
            right -= 1

        return ans
