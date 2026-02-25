class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        threshold =  int(len(nums)/3 )
        
        


        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1    


        answer = []
        for key in freq:
            if freq[key] > threshold:
                answer.append(key)

        return answer
