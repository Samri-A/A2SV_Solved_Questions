class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3

        piles.sort(reverse = True)

        mycoins = 0
        coins_len = 0

        for i in range(1 , len(piles) , 2 ):
            if coins_len < n:
               mycoins += piles[i]
               coins_len += 1
            else:
                break

        return mycoins

