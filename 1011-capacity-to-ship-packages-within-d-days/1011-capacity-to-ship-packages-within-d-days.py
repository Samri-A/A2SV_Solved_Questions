class Solution:
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def is_possible(capacity):

            days_c = 0
            current = 0
            for w in weights:
                current += w
                if current == capacity:
                    days_c += 1
                    current = 0
                elif current > capacity:
                    days_c += 1
                    current = w

            if current != 0:
                days_c+=1

            return days_c <= days

 

        left = max(weights)

        right = sum(weights)

        

        while left < right:
            mid = (left + right ) // 2
            if is_possible(mid):
                right = mid
            else:
                left = mid + 1

        return left



      


        