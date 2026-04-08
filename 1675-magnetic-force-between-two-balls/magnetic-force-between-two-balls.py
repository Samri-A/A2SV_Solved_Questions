class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()

        def can_be_placed(gap):
            balls = 1

            last = position[0]
            for i in range(1, len(position)):
                if position[i] - last >= gap:
                    balls+=1
                    last = position[i] 

            return balls >= m

        left = 1

        right = position[-1] - position[0] 

        

        while left <= right:

            mid = (right + left )//2

            if can_be_placed(mid):
                left = mid + 1
            else:
                right = mid - 1



        return right
