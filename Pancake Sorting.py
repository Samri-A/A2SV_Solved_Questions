class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []
        n = len(arr)

        for i in range(n, 0 , -1):
            k = arr.index(i)

            if k == i -1:
                continue 
            
            if k != 0:
                arr[:k+1] = arr[:k+1][::-1]
                answer.append(k+1)

            arr[:i] = arr[:i][::-1]
            answer.append(i)
        return answer
