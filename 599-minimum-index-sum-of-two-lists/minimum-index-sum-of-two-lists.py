class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common = []
        min_val = len(list2) + len(list1)
        for j in range(len(list1)):
            for i in range(len(list2)):
                if list2[i] == list1[j]:
                    if i + j < min_val:
                        min_val =  i + j
                        common = [list1[j]]
                    elif i + j == min_val:    
                        common.append(list1[j])
                    break
        
        return common

        