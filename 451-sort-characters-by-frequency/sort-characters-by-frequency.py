class Solution:
    def frequencySort(self, s: str) -> str:
        char_to_match ={
        }
        print(char_to_match)
        
        for i in range(len(s)):
            if s[i] not in char_to_match:
                char_to_match[s[i]] = 1
            else:
                char_to_match[s[i]] += 1
        
        
        sorted_dict = dict(sorted(char_to_match.items(), key=lambda item: item[1],      reverse=True))
        
        output = ''
        for k , v in sorted_dict.items():
            output += f'{k}' * v
        
        return output
                