class Solution(object):
    def count_frequency_of_word( self, word , freq):
        for i in word:
                if i in freq:
                    freq[i] += 1
                else: 
                    freq[i] = 1
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False

        word1_freq = {}
        word2_freq = {}
        freq1= []
        freq2 = []
        shorted_word1= "".join(sorted(word1))
        shorted_word2=  "".join(sorted(word2))
        if shorted_word1 == shorted_word2 :
            return True
        else :
            self.count_frequency_of_word(shorted_word1 , word1_freq)
            self.count_frequency_of_word(shorted_word2 , word2_freq)
            word1_un = []
            word2_un = []
            for key in word1_freq:
                freq1.append(word1_freq[key])
                word1_un.append(key)
            for key in word2_freq: 
                freq2.append(word2_freq[key])
                word2_un.append(key)
            if len(word1_un) != len(word2_un):
                return False
            for i in range(len(word1_un)):
                if word1_un[i] != word2_un[i]:
                    return False

            freq1.sort()
            freq2.sort()

            for i in range(len(freq1)):
                if freq1[i] != freq2[i]:
                    return False
            
            
        return True
        