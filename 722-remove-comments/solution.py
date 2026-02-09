from collections import deque
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        answer = []
        stack = deque()
        for line in source:
            if len(stack) == 0:
                temp = ""
            i = 0
            while i < len(line):
                if stack: 
                    if line[i] == '*':
                        if i + 1 < len(line) and  line[i+1] == '/':
                                stack.pop()
                                i += 2
                        else:
                                i+=1
                    else:
                            i+=1
                    continue
                if line[i] == '/':
                    if i + 1 < len(line):
                        if line[i+1] == '/':
                            break
                        elif line[i+1] == '*':
                            stack.append("/*")
                            i += 2
                        else:
                            if len(stack) == 0: temp += line[i] 
                            i+=1
                    else :
                            if len(stack) == 0: temp += line[i] 
                            i+=1
                    
                
                    
                elif len(stack) == 0:
                    temp += line[i] 
                    i += 1
                else:i += 1
            if len(temp) > 0 and len(stack) == 0 : answer.append(temp)
        return answer





