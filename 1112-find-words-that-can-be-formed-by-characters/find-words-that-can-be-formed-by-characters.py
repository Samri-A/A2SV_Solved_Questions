class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars = ''.join(sorted(chars))
        good_string = 0
        for i in range(len(words)):
            words[i] =  ''.join(sorted(words[i]))
        for i in words:
            pointer_c = 0
            pointer_i = 0

            while pointer_i < len(i) and pointer_c < len(chars):
                if chars[pointer_c] == i[pointer_i]:
                    pointer_i += 1
                    pointer_c += 1
                elif chars[pointer_c] > i[pointer_i]:
                    break
                else:  pointer_c += 1

            if pointer_i == len(i)   : good_string += len(i)

        return good_string

        

