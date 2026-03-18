class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost = 0
        B_A_diff = []
        for person_cost in costs:

            B_A_diff.append([person_cost[1] - person_cost[0] , person_cost[0] , person_cost[1]])
        
        
        B_A_diff.sort()

        for i in range(0, len(costs)//2):
            min_cost += B_A_diff[i][2]
        
        for i in range(len(costs)//2 , len(costs)):
            min_cost += B_A_diff[i][1]
            
        
        return min_cost
