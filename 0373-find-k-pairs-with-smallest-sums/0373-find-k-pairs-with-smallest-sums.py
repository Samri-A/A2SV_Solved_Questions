class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        # heapq.heapify(nums1)

        # heapq.heapify(nums2)

        sums = []
        visted = set()
        result = []

        heapq.heapify(sums)

        heapq.heappush( sums , (nums1[0] + nums2[0] , 0, 0 ))
        visted.add((0 , 0))

        while sums and len(result) < k:
            s , i , j = heapq.heappop(sums)

            result.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i+1 , j) not in visted:
                heapq.heappush( sums , (nums1[i+1] + nums2[j] , i+1, j ))
                visted.add((i+1 , j))
            
            if j + 1 < len(nums2) and (i , j + 1) not in visted:
                heapq.heappush( sums , (nums1[i] + nums2[j+1] , i, j+1) )
                visted.add((i , j+1))

        return result



                



       