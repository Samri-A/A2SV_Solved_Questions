class Solution:
    def smallestPalindrome(self, s: str) -> str:
         
        sorted_s = "".join(sorted(s))
        first_mirror = ""
        oddstr=""
        if len(sorted_s)%2 == 0:
            for i in range(0 , len(sorted_s) , 2):
                first_mirror+=sorted_s[i]
        else:
            middle = ''
            odd_freq = {}
            for i in sorted_s:
                odd_freq[i]=odd_freq.get(i,0)+1
                
                
            for key in odd_freq:
                
                if odd_freq[key]%2 == 0:
                    first_mirror += key * (odd_freq[key]//2) 
                
                else:
                    if odd_freq[key] > 1:
                        first_mirror += key * ((odd_freq[key]- 1)//2) 
                        middle = key
                    else:
                         middle = key 
                    
                
        print(first_mirror)
        mirrored = first_mirror[::-1] 
        print(mirrored)
       
        
        if len(sorted_s)%2 == 0:
            return  first_mirror+mirrored    
        else:  return  first_mirror + middle + mirrored