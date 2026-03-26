class Solution:
    def combination(self ,  n , k , path , arr):
        

        if len(path) == k:
            arr.append(path.copy())
            return 
            

        for i in range(1, n) :
            path.append(i)
            self.combination( i , k , path , arr)
            path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        self.combination(n+1, k , [] , arr)
        return arr

#         def backtrack(s, partial, remaining):
# if is_solution(partial):
# return partial
# for c in remaining:
# # Error: modifying iterable while iterating
# remaining.remove(c)
# backtrack(s, partial+c, remaining)
# remaining.append(c)