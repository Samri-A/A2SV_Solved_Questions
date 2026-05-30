class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        choosen = set(banned)
        sum_ = 0
        count = 0
        for i in range(1, n+1):
            if i not in choosen and (sum_ + i) <= maxSum:
                count += 1
                sum_ += i

        return count
