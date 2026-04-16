from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {}

        current = 1

        result = []
        for i in range(len(nums)):

            


            if nums[i] in freq and freq[nums[i]] == 1:
                result.append(nums[i])
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

            if current != nums[i]:
                result.append(current)
            current+=1
            

        # print(freq)

        

        return result

