class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        subarray_sum = {0: 1}
        count = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum+=num

            if prefix_sum%k in subarray_sum:
                count += subarray_sum[prefix_sum%k ]

            if prefix_sum%k in subarray_sum :
                 subarray_sum[prefix_sum%k] += 1
            else: subarray_sum[prefix_sum%k] = 1

        return count
        
