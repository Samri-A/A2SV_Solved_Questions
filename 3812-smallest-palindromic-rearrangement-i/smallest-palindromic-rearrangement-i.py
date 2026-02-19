class Solution:
    def smallestPalindrome(self, s: str) -> str:

        # for ex : daccad. consider the length also when it is even and odd
        # first letter = a
        # if it is odd there must be a letter that is not a pair ( like aca : c is one) so we put that letter in the middle 
        # and we will append the next lexicographic charachter 
        # """is not it better if we sort them first so it will be easy to find""" what about using min to find the smallest lexical one 
        
                
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
                         middle = key #we have to make this odd str cause it is the last part malt ok chershi ena i will let you know wht i am thinking
                    
                
        print(first_mirror)
        mirrored = first_mirror[::-1] 
        print(mirrored)
       
        
        if len(sorted_s)%2 == 0:
            return  first_mirror+mirrored    #yeah i am trying to sort it kelay but forgot the syntax
        else:  return  first_mirror + middle + mirrored