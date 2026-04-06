class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()
        
        heater_p = 0
        houses_p = 0

        min_radius = 0

        while houses_p < len(houses):


            

            while heater_p + 1 < len(heaters):
                if abs(houses[houses_p] - heaters[heater_p]) >= abs(houses[houses_p] - heaters[heater_p + 1]):
                    heater_p+=1
                else:
                    break

            min_radius = max(abs(houses[houses_p] - heaters[heater_p])  , min_radius )

            
            houses_p+=1

        return min_radius

        # 