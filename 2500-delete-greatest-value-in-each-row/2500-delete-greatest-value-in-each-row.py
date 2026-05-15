class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:


        for row in range(len(grid)):
            grid[row].sort()

        answer = 0

        for i in range(len(grid[0])):

            max_answer = 0

            for j in range(len(grid)):
                max_answer = max(grid[j][i] , max_answer)

            answer += max_answer


        print(grid)


        return answer