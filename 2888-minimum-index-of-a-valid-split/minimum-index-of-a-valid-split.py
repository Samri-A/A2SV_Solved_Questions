from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        dominant_element = 0
        max_freq = 0
        for key in freq:
            if max_freq < freq[key]:
                max_freq = freq[key]
                dominant_element = key
        
        print(dominant_element)
        
        f1 = 0
        f2 =  max_freq
        for i in range(len(nums)):
            if nums[i] == dominant_element:
                f1+=1
                f2 -=1
                print(i , f1 , f2)

            if f1 > ((i+1)//2) and f2 > (((len(nums)-i-1))//2):
                return i

            
        return -1
             
        