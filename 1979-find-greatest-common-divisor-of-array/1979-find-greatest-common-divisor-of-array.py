import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        sm = min(nums)
        lg = max(nums)

        val = math.gcd(sm , lg)

        return val

