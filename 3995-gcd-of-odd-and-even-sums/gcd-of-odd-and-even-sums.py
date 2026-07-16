import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        old_sum = n * n
        even_sum = n * (n+1)

        gcd = math.gcd( old_sum , even_sum)


        return gcd