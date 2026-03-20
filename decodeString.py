class Solution:
    def decodeString(self, s: str) -> str:
        
        decoded_str = ""

        stack = []
        
        for i in range(len(s)):

            if s[i] == ']':
                substr = ""
                while stack and stack[-1] != '['  :
                    substr = stack.pop() + substr

                stack.pop() 
                number = ""

                while stack and str(stack[-1]).isdigit():
                    number = stack.pop() + number

                print(number)
                stack.append( int(number) * substr )
            else:
                
                stack.append(s[i])

        
        while stack:
            decoded_str = stack.pop() + decoded_str

        return decoded_str


            

