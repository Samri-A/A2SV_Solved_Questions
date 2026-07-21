class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        s = "1" + s + "1"

        counter = []

        for i in range(1 , len(s)-1):
            if s[i] == "0":
                if counter and counter[-1] <  0 :
                    counter[-1] -= 1
                else:
                   counter.append(-1)
            else:
                if counter and counter[-1] >  0 :
                    counter[-1] += 1
                else:
                   counter.append(1)

        ones = 0
        for i in range(1 , len(s)-1):
            if s[i] == "1":
                ones+=1
             


        max_sum = 0

        for i in range(1 , len(counter)-1):
            if counter[i-1] < 0 and counter[i+1] < 0 :
                gain = abs(counter[i-1]) + abs(counter[i+1])
                max_sum = max(max_sum , gain+ones)
              

        if max_sum < ones:
            return ones 
            
        return max_sum