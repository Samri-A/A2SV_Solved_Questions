from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        answer = []
        for key in count1:
            if key in count2:
                answer.append(key)

        return answer

        