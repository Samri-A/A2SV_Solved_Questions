class Solution:
    def tribonacci(self, n: int) -> int:

        T_array = [1] * (n + 3)

        T_array[0] = 0
        T_array[1] = 1
        T_array[2] = 1

        i = 0
        while i < n:

            T_array[i+3] = T_array[i] + T_array[i+1] + T_array[i+2]
            i += 1

        return T_array[i]





        