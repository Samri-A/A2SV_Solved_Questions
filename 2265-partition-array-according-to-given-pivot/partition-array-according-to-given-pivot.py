class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        greater = []
        equal = 0

        for num in nums:
            if num == pivot:
                equal += 1
            elif num < pivot:
                smaller.append(num)
            else:
                greater.append(num)
        
        for i in range(equal , 0 , -1):
            smaller.append(pivot)

        smaller.extend(greater)

        return smaller
        