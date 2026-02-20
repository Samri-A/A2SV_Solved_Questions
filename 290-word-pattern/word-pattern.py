class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False

        letter_to_word = {}
        word_to_letter = {}

        index_of_s = 0
        for i in words:

            if pattern[index_of_s] in letter_to_word:
                if i != letter_to_word[pattern[index_of_s]]:
                    return False
            else:
                letter_to_word[pattern[index_of_s]] = i 


            if i not in word_to_letter:
                word_to_letter[i] = pattern[index_of_s]
                
            else:
                if word_to_letter[i] != pattern[index_of_s] :
                    return False
            
            index_of_s+=1
        
        return True
        