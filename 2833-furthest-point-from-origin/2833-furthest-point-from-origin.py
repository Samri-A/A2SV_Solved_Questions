class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        point = 0
        n = len(moves)

        r = moves.count("R")
        l = moves.count("L")

        

        if r > l:
            replace = "R"
        else:
            replace = "L"

        arr = []
        for i in range(n):
            if moves[i] == "_":
                arr.append(replace)
            else:
                arr.append(moves[i])





        

        for i in range(n):

            if arr[i] == "R": 
                    point+=1
                    
            else:
                point -= 1
            print(arr[i]  , point)

        return abs(point)

