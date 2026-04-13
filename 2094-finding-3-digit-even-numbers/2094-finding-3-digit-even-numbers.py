class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        # digits.sort()
        path = []
        answer = set()

        used = [False] * len(digits)

        def concat_3():

            if len(path) == 3:
                temp = "".join(path)
                answer.add(int(temp))
                return

            
            for i in range(len(digits)):
                if used[i]:
                    continue 

                # if i > 0 and digits[i-1] == digits[i]:
                #      continue
                
                if len(path) == 0 and digits[i] == 0:
                    continue
                
                if len(path) == 2 and digits[i]%2 != 0:
                    continue

                used[i] = True
                path.append(str(digits[i]))
                concat_3()
                used[i] = False
                path.pop()

            # print(path)

        
        concat_3()
        return sorted(list(answer))

            
