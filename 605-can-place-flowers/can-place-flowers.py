class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if flowerbed[0]:
            start = 2
        else:
            start = 0


        pointer = 0

        flower = 0

        if len(flowerbed) == 1:
            if (n <= 1 and not flowerbed[0]) or (n == 0 and flowerbed[0] ) :
                return True
            else:
                return False

        while pointer < len(flowerbed):

            if flowerbed[pointer]== 0:

                if pointer + 1 < len(flowerbed):
                    if flowerbed[pointer + 1] == 0: 
                        if pointer - 1 < 0:
                            flowerbed[pointer] = 1
                            flower += 1
                        elif flowerbed[pointer - 1] == 0 :
                            flowerbed[pointer] = 1
                            flower += 1

                elif flowerbed[pointer - 1] == 0:
                    flower += 1

            pointer += 1


        if flower >= n:
            return True
        else:
            return False
                        