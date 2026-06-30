class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        A121 = 6
        A123 = 6

        for i in range(2, n+1):
            A121 , A123=( A121 * 3) +( A123 * 2) , ( A123 * 2 )+ (A121 * 2)

        return (A123 + A121)%MOD