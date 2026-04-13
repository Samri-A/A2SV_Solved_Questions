class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        oper = {"+": 1, "-": 1, "*": 1}

        def compute(left, right):

            res = []

            for i in range(left, right + 1):
                if expression[i] in oper:

                    left_nums = compute(left, i - 1)
                    right_nums = compute(i + 1, right)

                    for left_num in left_nums:
                        for right_num in right_nums:
                            if expression[i] == "+":
                                res.append(left_num + right_num)
                            elif expression[i] == "-":
                                res.append(left_num - right_num)
                            elif expression[i] == "*":
                                res.append(left_num * right_num)

            if len(res) == 0:
                return [int(expression[left : right + 1])]

            return res

        return compute(0, len(expression) - 1)
