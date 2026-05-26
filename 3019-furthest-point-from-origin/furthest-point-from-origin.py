class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        point = 0
        n = len(moves)

        r = moves.count("R")
        l = moves.count("L")
        

        for i in range(n):

            if moves[i] == "R": 
                    point+=1
                    
            elif moves[i] == "L":
                point -= 1
            else:
                if r > l:
                    point+=1
                else:
                    point -= 1

        return abs(point)

