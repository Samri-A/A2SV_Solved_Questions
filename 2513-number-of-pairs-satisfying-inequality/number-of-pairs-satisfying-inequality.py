class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        diff_arr = []

        n = len(nums1)

        for i in range(n):
            diff_arr.append(nums1[i] - nums2[i])

        print(diff_arr)

        result = [0]


        def merge_sort(arr):

            if len(arr) <= 1:
                return arr

            
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

             

            j = 0
            for l in left:
                
                while j < len(right) and (l - right[j]) > diff:
                    j += 1
                
                result[0] += len(right) - j

            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        
        merge_sort(diff_arr)

        return result[0]