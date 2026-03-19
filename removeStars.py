class Solution:
    def removeStars(self, s: str) -> str:
        
        char_stack = []

        for c in s:
            if c == '*':
                if char_stack:
                    char_stack.pop()
            else:
                char_stack.append(c)

        return "".join(char_stack)
        # print(char_stack)
