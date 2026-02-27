def subarraysWithNotMorethanKDistinct(nums, k) -> int:
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

            while distinct > k and left < len(nums):
                    prefix = 0
                    if count_freq[nums[left]] > 1:
                        count_freq[nums[left]] -=1 
                    else :
                        distinct -= 1
                        del count_freq[nums[left]]
                    left +=1

            if distinct <= k:
                while nums[left] in count_freq and count_freq[nums[left]] > 1 and left < len(nums):
                    count_freq[nums[left]] -= 1
                    left += 1
                    prefix+=1
                count_subarray += prefix + right - left + 1
                
                

            right += 1
        return count_subarray

n , k = map(int , input().split()) 
nums = list(map(int , input().split()))
if n == 0 or k == 0:
     print(0)
     exit()
answer = subarraysWithNotMorethanKDistinct(nums=nums , k=k)
print(answer)
