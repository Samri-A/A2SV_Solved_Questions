class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        # 75 10
        coin_75 = x 
        coin_10 = y // 4

        turn = min(coin_75 , coin_10)

        # print(turn)



        if turn%2 == 0 :
            return "Bob"
        else:
            return "Alice"

 
