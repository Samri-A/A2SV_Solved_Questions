class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        prefix = 0
        count_freq = {}
        count_subarray = 0
        distinct = 0
        while right < len(nums):

            if nums[right] in count_freq:
                count_freq[nums[right] ]+= 1
            else:
                distinct += 1
                count_freq[nums[right]] = 1

            while distinct > k:
                    prefix = 0
                    if count_freq[nums[left]] > 1:
                        count_freq[nums[left]] -=1 
                    else :
                        distinct -= 1
                        del count_freq[nums[left]]
                    left +=1

            if distinct == k:
                while count_freq[nums[left]] > 1:
                    count_freq[nums[left]] -= 1
                    left += 1
                    prefix+=1
                count_subarray += prefix+1
                
                

            right += 1
        return count_subarray
