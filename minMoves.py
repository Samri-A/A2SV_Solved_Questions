class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        
        while maxDoubles > 0 and target > 1:
                moves += target%2

                target = target//2

                moves += 1

                maxDoubles -=1

        # print(moves)
        # print(target)

        if target == 1:
            return moves
        else:
            return moves + target - 1 

            
        
