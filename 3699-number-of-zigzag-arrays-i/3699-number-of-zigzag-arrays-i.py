class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        
        m = 1000000007

        n_ = r - l + 1

        dp = [1] * n_

        for _ in range(2, n+1):

            dp.reverse()

            pref = 0

            for i in range(n_):

                prev = dp[i]

                dp[i] = pref

                pref =  (pref + prev) % m

        ans = sum(dp) % m


        return (ans * 2) % m


