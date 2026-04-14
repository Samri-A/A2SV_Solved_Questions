from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        answer = []

        nums = list(range(1, n+1))
       
        k -=1 
        
        
        while nums:

            block_size = factorial(len(nums)-1)

            index = k//block_size

            answer.append(str(nums[index]))
            nums.pop(index)

            k = k%block_size



        return ''.join(answer)
