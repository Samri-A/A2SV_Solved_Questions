class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """


        responses_counter = {}
        for response  in responses:
            unique_response = []
            track_response = {}
            for j in response:
                if j in track_response:
                    continue 
                else:
                    track_response[j] = 1
                    unique_response.append(j)
                
            
            for i in unique_response:
                if i in responses_counter:
                    responses_counter[i] += 1 
                else:
                    responses_counter[i] = 1

        max_val = 0
        max_key = ''
        for key in responses_counter:
            if responses_counter[key] > max_val:
                max_val = responses_counter[key]
                max_key = key
            elif responses_counter[key] == max_val and key < max_key: max_key = key
        return max_key