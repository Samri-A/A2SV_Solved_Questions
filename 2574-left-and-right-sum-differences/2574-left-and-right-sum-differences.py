class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)


        ls = 0
        for i in range(len(nums)):

            leftSum[i] = ls  
            ls +=  nums[i]

        rs = 0
        for j in range(len(nums)-1 , -1 , -1):

            rightSum[j] = rs  
            rs += nums[j]

        # print(leftSum)
        # print(rightSum)


        ans = [0] * len(nums)

        for i in range(len(nums)):
            ans[i] = abs(leftSum[i] - rightSum[i])

        return ans
