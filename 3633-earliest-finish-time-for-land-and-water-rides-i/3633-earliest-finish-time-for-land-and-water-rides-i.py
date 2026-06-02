class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        

        min_possible_time = float('inf')

        for i in range(len(landStartTime)):
            end = landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                ans = max(waterStartTime[j] ,end ) + waterDuration[j]  
                min_possible_time = min(ans , min_possible_time)

        for i in range(len(waterStartTime)):
            end = waterStartTime[i] + waterDuration[i]
            for j in range(len(landDuration)):
                    ans = max(landStartTime[j] , end )+landDuration[j] 
                    min_possible_time = min(ans , min_possible_time)

        return min_possible_time
