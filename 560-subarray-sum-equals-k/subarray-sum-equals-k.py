class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_sum_freq = { 0 : 1}
        c = 0
        result = 0
        sumation = 0
        for i in nums:
            sumation += i
            if sumation - k in  subarray_sum_freq:
                result+= subarray_sum_freq[sumation - k]

            if sumation in subarray_sum_freq : subarray_sum_freq[sumation] += 1
            else:
                subarray_sum_freq[sumation] = 1

        return result
        