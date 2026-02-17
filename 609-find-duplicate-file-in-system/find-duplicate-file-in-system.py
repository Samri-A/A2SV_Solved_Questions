class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        file_content_tracker = {}
        for i in paths:
            val =  i.replace( "(", " ").replace(")", "").split()
            temp = val[0]
            filecontent = ''
            j = 2
            while j < len(val):
                filecontent = val[j]
                temp_path = temp + '/' + val[j-1]
                
                if filecontent not in file_content_tracker:
                            file_content_tracker[filecontent] = []
                file_content_tracker[filecontent].append(temp_path)
                j+=1
            # for j in reversed(val):
            #     if 'root' in j:
            #         continue 
            #     elif 'txt' in j:
            #         temp_path = temp + '/' + j
            #         if filecontent != ' ': 
            #             file_content_tracker[filecontent].append(temp_path)
            #     else:
            #         if j != ' ':
            #             filecontent = j
            #             if filecontent not in file_content_tracker:
            #                 file_content_tracker[filecontent] = []


        answer = []
        
        for key in file_content_tracker:
            if len(file_content_tracker[key]) > 1:
                answer.append(file_content_tracker[key])
       
        return answer