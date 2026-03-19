class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []

        greater_map = {}

        for num in reversed(nums2):

            if len(stack) == 0:
                stack.append(num)
                greater_map[num] = -1
            else:
                
                if stack[-1] < num:
                    while len(stack) > 0 and stack[-1] < num:
                        stack.pop()
                    if len(stack) > 0:  greater_map[num] = stack[-1]
                    else:  greater_map[num] = -1
                    stack.append(num)
                else:
                    greater_map[num] = stack[-1]
                    stack.append(num)
                    # stack.pop()


        answer = [greater_map[num] for num in nums1]

       
        return answer
