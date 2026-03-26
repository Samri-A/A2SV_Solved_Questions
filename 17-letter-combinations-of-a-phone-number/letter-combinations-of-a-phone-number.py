class Solution:
    
    


        
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []
        
        phone_book ={ 
            1:[], 
            2: ['a' , 'b' , 'c'],
            3: ['d' , 'e' , 'f'],
            4: ['g' , 'h' , 'i'],
            5: ['j' , 'k' ,'l'],
            6: ['m' , 'n' , 'o'],
            7: ['p' , 'q' , 'r' , 's'],
            8: ['t' , 'u' , 'v' ], 
            9 : ['w' , 'x' , 'y' , 'z']
        }

        i = -1
        arr = []
        path = []
        def combineletter(i):
            if len(path) == len(digits):                
                arr.append("".join(path))
                return

            i += 1
            for char in phone_book[int(digits[i])]:
                path.append(char)
                combineletter(i)
                path.pop()

        combineletter(i)

        return arr