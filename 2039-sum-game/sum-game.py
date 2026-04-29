class Solution:
    def sumGame(self, num: str) -> bool:
        
        left_ques = 0
        right_ques = 0

        left_sum = 0
        right_sum = 0

        for i in range(len(num)):

            if num[i] == '?':
                if i < len(num)//2: left_ques+=1
                else: right_ques+=1
            else:
                if i < len(num)//2: left_sum+= int(num[i])
                else: right_sum += int(num[i])

        print(left_ques , right_ques)
        print(left_sum , right_sum)

        if (left_ques + right_ques)%2 == 1:
            return True

        if (left_sum - right_sum) == 9 * ((right_ques - left_ques) / 2 ) :
            return False
        

        return True
         

