class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        def split( index   , count , prev):

            if index == n:
                return count >= 2

            
            current = 0
            for end in range( index  , n):

                current = current * 10 + int(s[end])

                if prev is None:
                    if split(end +1  ,count+1 , current):
                        return True

                else:
                    if current == prev - 1:
                        if split(end + 1 ,count+1 , current):
                            return True

                    if current  > prev - 1:
                        break

            return False



        return split(0 , 0 , None)

        
                    



