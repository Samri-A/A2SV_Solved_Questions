class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = []
        L = 0

        for letter in s:
            if letter == "*":
                L = max(0 , L-1)
            elif letter == "#":
                L = L * 2
            elif letter == "%":
                pass
            else:
                L += 1
            
            length.append(L)

        if L <= k:
            return "."

        for i in range(len(s)-1 , -1 , -1):
            ch = s[i]
            current_len = length[i]
            prev_len = length[i-1] if i > 0 else 0

            if ch not in "*#%":
                if k == current_len - 1:
                    return ch
            elif ch == "#":
                if prev_len > 0 and k >= prev_len:
                    k -=   prev_len
            elif ch == "%":
                k = current_len - k -1

        
        return "."

        