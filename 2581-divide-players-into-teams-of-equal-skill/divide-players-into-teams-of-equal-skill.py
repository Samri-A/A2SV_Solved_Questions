class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # sum_of_skills = 0
        # for i in skill:
        #     sum_of_skills+=i

        # # Check if we can divde the skills equally
        # if sum_of_skills%2 != 0:
        #     return -1

        sum_of_team_chemistry = 0
        left = 0
        right = len(skill) - 1
        skill.sort()
        match = skill[left] + skill[right]
        while left < right:
            if skill[left] + skill[right] == match:
                sum_of_team_chemistry += skill[left] * skill[right]
            else:
                return -1
            left+=1
            right-=1

        return sum_of_team_chemistry