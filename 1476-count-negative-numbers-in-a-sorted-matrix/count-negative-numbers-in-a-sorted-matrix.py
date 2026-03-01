class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative_numbers = 0

        for i in grid:
            right = len(i) - 1

            while right >= 0 :
              if i[right] < 0:
                negative_numbers+=1
                right -=1
              else:
                break

        return negative_numbers
