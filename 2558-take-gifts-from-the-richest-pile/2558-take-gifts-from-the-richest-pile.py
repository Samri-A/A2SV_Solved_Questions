import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        arr = [ -gift for gift in gifts]
        heapq.heapify(arr)


        
        while k > 0:

            num = - heapq.heappop(arr)

            newnum = math.floor(num ** 0.5)

            heapq.heappush(arr ,-newnum )

            
            k-=1

        return - sum(arr)

        