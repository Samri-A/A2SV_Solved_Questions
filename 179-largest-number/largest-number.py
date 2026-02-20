class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert the numbers to string
        str_num = []
        for i in nums:
            str_num.append(str(i))

        # We define comparison function
        def compsre_pair(n1 , n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1

        str_num = sorted(str_num , key =cmp_to_key(compsre_pair))

        for i in nums:
            if i != 0 :
                return ''.join(str_num)
        
        return '0'