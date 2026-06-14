class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:

        ans = ""
        
        i = 0

        dic = {i : chr(ord('z')- i) for i in range(26)}

        dic_letter = { chr(ord('a')+ i)  : weights[i] for i in range(len(weights))}
        

        

        a = weights[i]

        for word in words:
            temp_sum = 0

            for letter in word:
                temp_sum += dic_letter[letter]
                i+=1

            l = temp_sum%26
            # print(l)

            ans += dic[l]

        return ans



            

