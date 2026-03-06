class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        smoothed_img = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
            # [0] for _ in img[0]] * len(img)
        print(smoothed_img)
        for row in range(len(img)):
            for col in range(len(img[0])):

                sumation = 0
                n = 0
                sumation += img[row][col]
                n+=1
                if col - 1 >= 0:
                        sumation += img[row][col-1]
                        n+=1

                if col + 1 < len(img[0]):
                        sumation += img[row][col+1]
                        n+=1
                if row - 1 >= 0:
                    sumation += img[row-1][col]
                    n+=1
                    if col - 1 >= 0:
                        sumation += img[row-1][col-1]
                        n+=1

                    if col + 1 < len(img[0]):
                        sumation += img[row-1][col+1]
                        n+=1

                if row + 1 < len(img):
                    sumation += img[row+1][col]
                    n+=1
                    if col - 1 >= 0:
                        sumation += img[row+1][col-1]
                        n+=1

                    if col + 1 < len(img[0]):
                        sumation += img[row+1][col+1]
                        n+=1

                smoothed_img[row][col] = sumation//n

        return smoothed_img
                    
                    
