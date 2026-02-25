class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)

        small_end = points[0][1]
        size = 0
        arrow = 0

        if len(points) == 1: return 1

        for i in points:
            if i[0] <= small_end  :
                if i[1] <= small_end:
                    small_end = i[1]
                size+=1
            else:
                arrow += 1
                small_end = i[1]
                size = 1
            print(small_end , size  , arrow)

        if size != 0:
            arrow+=1

        return arrow



        
