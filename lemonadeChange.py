# from collections import Counter
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # change = Counter(bills)

        change_5 = 0
        change_10 = 0

        for bill in bills:
            if bill > 5:
                temp = bill - 5
                if temp > change_5 + change_10 or  change_5 == 0:
                    return False
                else:
                   if temp == 5: 
                    change_5-= 5
                    change_10 +=10
                   else: 
                    change_10 -=10
                    change_5 -= 5
            else:
                change_5+=5 

        return True

                

