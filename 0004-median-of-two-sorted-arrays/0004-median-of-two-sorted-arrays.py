class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        median = 0.0
        
        merged_num = []
        
        pointer_1 = 0
        pointer_2 = 0

        while pointer_1 < len(nums1) and pointer_2 < len(nums2):
            if nums1[pointer_1] <= nums2[pointer_2]:
                merged_num.append(nums1[pointer_1])
                pointer_1+=1
            else:
                merged_num.append(nums2[pointer_2])
                pointer_2+=1

        

        while pointer_1 < len(nums1):
            merged_num.append(nums1[pointer_1])
            pointer_1+=1
        
        while pointer_2 < len(nums2):
            merged_num.append(nums2[pointer_2])
            pointer_2+=1



        if len(merged_num)%2:
            median = merged_num[len(merged_num)//2 ]
        else:
            return (merged_num[len(merged_num)//2] + merged_num[len(merged_num)//2 - 1])/2
        return median