class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()


        i = len(cost)-1

        total = 0

        while i >= 0:

            total += cost[i]

            i -= 1

            if i >= 0:
                total += cost[i]
            
            i-=2

        return total

