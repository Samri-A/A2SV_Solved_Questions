class Solution:
    

    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def myPow(x , n):

            result = 1

            while n > 0:
                if n%2:
                    result = (result * x) %MOD

                n = n//2
                x =( x * x) %MOD

            return result
                

        
        if n%2 == 0:
            return (myPow(4, n//2) *  myPow(5, n//2)) %MOD
        else:
            return (myPow(4, n//2) *  myPow(5, n//2 + 1))%MOD
        
        
         
