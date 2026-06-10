import heapq
import math
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        n = len(nums)

        # logs
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        m = lg[n] + 1

        # sparse tables
        mx = [nums[:]]
        mn = [nums[:]]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1

            mx_row = []
            mn_row = []

            for i in range(n - length + 1):
                mx_row.append(
                    max(mx[j - 1][i],
                        mx[j - 1][i + half])
                )

                mn_row.append(
                    min(mn[j - 1][i],
                        mn[j - 1][i + half])
                )

            mx.append(mx_row)
            mn.append(mn_row)
            j += 1

        def value(l, r):
            p = lg[r - l + 1]

            maximum = max(
                mx[p][l],
                mx[p][r - (1 << p) + 1]
            )

            minimum = min(
                mn[p][l],
                mn[p][r - (1 << p) + 1]
            )

            return maximum - minimum

        heap = []

        for l in range(n):
            r = n - 1
            heapq.heappush(
                heap,
                (-value(l, r), l, r)
            )

        ans = 0

        for _ in range(k):
            negv, l, r = heapq.heappop(heap)

            ans += -negv

            if r > l:
                nr = r - 1
                heapq.heappush(
                    heap,
                    (-value(l, nr), l, nr)
                )

        return ans 