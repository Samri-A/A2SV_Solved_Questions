class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        
        jumps = []
        heapq.heapify(jumps)

        i = 0

        while i < len(heights)-1:

            jump = heights[i+1] - heights[i]

            if jump > 0 :
                heapq.heappush( jumps, jump)
                
                if len(jumps) > ladders:
                    bricks -= heapq.heappop(jumps)
                    
                if bricks < 0:
                    return i

            i+=1
        
        return i
                
                
            