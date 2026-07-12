class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        newarr = [[arr[i] , i] for i in range(len(arr))]
        newarr.sort( key = lambda x : x[0])
        ans = [0] * len(arr)

        rank = 1
        ans[newarr[0][1]] = 1
        prev = newarr[0][0]
        for  i in range(1,len(newarr)):
            if prev != newarr[i][0]:
                rank += 1
            ans[newarr[i][1]]= rank
            prev = newarr[i][0]
            
        print(newarr)

        return ans