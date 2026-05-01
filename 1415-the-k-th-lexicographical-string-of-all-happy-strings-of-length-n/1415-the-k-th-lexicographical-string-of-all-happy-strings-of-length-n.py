class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        result = []

        letters = ['a' , 'b' , 'c']

        path = []

        def backtrack():

            if len(path) == n:
                temp = "".join(path)
                result.append(temp)
                return 

            
            
            for char in letters:

                if path and path[-1] == char:
                    continue

                path.append(char)
                backtrack()
                path.pop()

        
        backtrack()

        

        if k > len(result):
            return ""

        result.sort()


        return result[k - 1]





