class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq = [0] * (len(nums)+1)

        for request in requests:
            freq[request[0]] += 1 
            freq[request[1] + 1] -= 1

        
        current = 0

        requests_freq = [0] * (len(nums))

        for i in range(len(requests_freq)):
            
            current += freq[i]
            requests_freq[i] += current

        
       

        
        requests_freq.sort(reverse=True)
        nums.sort(reverse=True)
        
        answer = 0

        j = 0

        for i in range(len(requests_freq)):
            if requests_freq[i] == 0: break
            answer += (requests_freq[i] * nums[j])
            j+=1

        


        modulo = 10**9 + 7
        return answer%modulo