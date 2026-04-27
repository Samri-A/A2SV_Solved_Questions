class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0


       

        
        

        l , h = min(nums) , max(nums)

        if l == h : return 0

        gap = max(1, (h - l )// (len(nums)-1))

        buckets = [[None,None] for _ in range((h-l)//gap + 1)]


        for num in nums:
            

            index = (num-l)//gap

            if buckets[index][0] is None:
                buckets[index][0] = num
                buckets[index][1] = num
            else:
                buckets[index][0] = min( buckets[index][0] , num)
                buckets[index][1] = max( buckets[index][1] , num)


        
        max_gap = 0
        prev_max = None

        for bmin , bmax in buckets:
            if bmin is None:
                continue
            
            if prev_max is not None:
                max_gap = max( bmin - prev_max, max_gap)


            prev_max = bmax


        return max_gap

        



        



