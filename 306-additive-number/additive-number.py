class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        

        def helper(first , second , remaining):

            if first[0] == '0' and len(first) != 1 :
                return False

            if  second[0]== '0' and len(second) != 1:
                return False

            # print(second)
            num1 = first

            num2 = second

            num3 = remaining

            sum_ = int(num1) + int(num2)

            # print(num1 , num2, num3)

            if len(num3) < len(str(sum_)):
                return False

            if sum_ == int(num3[:len(str(sum_))]):
                if len(str(sum_)) == len(num3):
                    return True
                
                first = num2
                second = num3[:len(str(sum_))]
                rem = num3[len(str(sum_)):]

                return helper(first , second , rem)
            

        index1 = 0

        for index2 in range(index1 + 1, len(num)):
            for index3 in range(index2 + 1, len(num)):
                first = num[:index2]
                second = num[index2 : index3]
                third = num[index3 : ]
                if max(len(first) , len(second)) > len(third):
                    continue
                if helper("".join(first) , "".join(second) , "".join(third)):
                    return True

        return False
        
