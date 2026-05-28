class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        

        digits = ""

        prev = None

        for i in range(len(s)):

            if s[i].isdigit():
                digits += s[i]
            else:
                if not digits:
                    continue

                if digits and prev:
                    if prev >= int(digits):
                        return False
                prev = int(digits)
                digits = ""

        if digits and prev and prev >= int(digits):
            return False

        return True