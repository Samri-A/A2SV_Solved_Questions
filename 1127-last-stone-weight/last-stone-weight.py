class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        arr = [-num for num in stones]

        heapq.heapify(arr)

        while len(arr) > 1:

            first_largest = - heapq.heappop(arr)
            second_largest = - heapq.heappop(arr)

            result = first_largest - second_largest

            if result > 0: heapq.heappush( arr , -result)
        
        if arr:
            return -arr[0]
        else:
            return 0