from collections import deque
class Solution:
    def calculate(self, s: str) -> int:

        sum_ = 0

        number = 0

        
        stack = []

        sign = 1

        for val in s:
            if val in "+-":
                sum_ += number * sign
                number = 0
                sign = -1 if val=='-' else 1
            elif val == '(':
                stack.append(sum_)
                stack.append(sign)
                number = 0
                sign = 1
                sum_ = 0

            elif val == ')':
                sum_ += number * sign
                number = 0

                prev_sign = stack.pop()
                prev_sum = stack.pop()

                sum_ = prev_sum + sum_ * prev_sign

            elif val.isdigit():
                number =  number*10 + int(val)


        sum_ += number * sign
        return sum_