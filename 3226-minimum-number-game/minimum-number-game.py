class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        arr = nums

        heapq.heapify(arr)

        result = []

        while arr:

            alice = heapq.heappop(arr)
            bob = heapq.heappop(arr)

            result.append(bob)
            result.append(alice)

        
        return result

