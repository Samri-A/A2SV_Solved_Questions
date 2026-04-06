class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {0:1}

        sum_ = 0

        count = 0

        for num in nums:

            sum_ += num

            if  sum_ - goal in prefix:

                count += prefix[ sum_ - goal]



            if sum_ in prefix: prefix[sum_] += 1
            else: prefix[sum_] = 1

            



        print(prefix)

        return count
