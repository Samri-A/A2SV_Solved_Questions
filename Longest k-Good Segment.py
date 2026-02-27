def longestSegementWithKDistinct(nums, k):
        left = 0
        right = 0
        count_freq = {}
        distinct = 0
        longest = 0
        longest_l , longest_r = 0 , 0
        
        while right < len(nums):

            if nums[right] in count_freq:
                count_freq[nums[right] ]+= 1
            else:
                distinct += 1
                count_freq[nums[right]] = 1

            while distinct > k and left < len(nums):
                    
                    if count_freq[nums[left]] > 1:
                        count_freq[nums[left]] -=1 
                    else :
                        distinct -= 1
                        del count_freq[nums[left]]
                    left +=1

            if distinct <= k:
                if  right - left + 1 > longest:
                    longest =  right - left + 1
                    longest_l = left
                    longest_r = right
                
                

            right += 1
        print(longest_l + 1 , longest_r + 1)

n , k = map(int , input().split()) 
nums = list(map(int , input().split()))
if n == 0 or k == 0:
     print(0 , 0)
     exit()
longestSegementWithKDistinct(nums=nums , k=k)
