class Solution:
    def reversePairs(self, nums: List[int]) -> int:

       


        def merge_sort(left , right):

            if right - left <= 1:
                return 0

            mid = (left + right )//2

            count = merge_sort(left , mid) + merge_sort(mid , right)

            
            j = mid

            for i in range(left , mid):
                while j < right  and nums[i] > nums[j] * 2:
                    j += 1

                count += j - mid
            
            nums[left:right] = sorted(nums[left:right]) 
            return count

        return merge_sort(0 , len(nums))



        