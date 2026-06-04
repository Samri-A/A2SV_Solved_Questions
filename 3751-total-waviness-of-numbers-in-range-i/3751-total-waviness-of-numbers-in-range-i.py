class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for i in range(num1 , num2+1):
            temp = str(i)
            if len(temp) == 3:
                if temp[0] < temp[1] > temp[2] or temp[0] > temp[1] < temp[2]:
                    total += 1
            elif len(temp) > 3:
                left  = 1
                while left < len(temp) - 1:
                    if temp[left - 1] < temp[left] > temp[left + 1] or temp[left - 1] > temp[left] < temp[left + 1]:
                        total += 1

                    left += 1

         
            print(total , i)

        return total