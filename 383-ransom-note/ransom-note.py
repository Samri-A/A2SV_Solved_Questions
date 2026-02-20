class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m_dic = {}
        
        for j in magazine:
            if j in m_dic:
                m_dic[j] += 1
            else :
                m_dic[j] = 1

        for i in ransomNote:
            if i not in m_dic:
                return False

            elif m_dic[i] == 1:
                del m_dic[i]
            else :
                m_dic[i] -= 1

        return True         