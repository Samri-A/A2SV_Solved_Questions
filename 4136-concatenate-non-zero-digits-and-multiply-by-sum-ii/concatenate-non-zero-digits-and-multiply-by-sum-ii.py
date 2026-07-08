class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        prefsum = []
        digits = []
        count = []
        mod = 10**9 + 7

        pre = 0
        num = 0
        c = 0
        for i in range(len(s)):

            x = int(s[i])
            if x!=0:
                num = (num * 10 + x)% mod
                c+=1
            pre += x
            prefsum.append(pre)
            digits.append(num)
            count.append(c)

        ans = []
        for l, r in queries:
            if l == 0:
                sum_ = prefsum[r]
                ans.append(sum_ * digits[r] % mod)

            else:
                sum_ = prefsum[r] - prefsum[l-1]

                before = count[l-1]
                after = count[r]

                if before == after:
                    ans.append(0)
                else:
                    length = after - before
                    remove = digits[l-1] * pow(10, length, mod)
                    num = (digits[r] - remove) % mod
                    ans.append(sum_ * num % mod)

        return ans
