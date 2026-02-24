class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
       

        sum_of_team_chemistry = 0
        left = 0
        right = len(skill) - 1

        # Sort to make matching 
        skill.sort()

        # get one valid match
        match = skill[left] + skill[right]

        # check if each pair equals to the match and return the team chemistry 
        while left < right:
            if skill[left] + skill[right] == match:
                sum_of_team_chemistry += skill[left] * skill[right]
            else:
                return -1
            left+=1
            right-=1

        return sum_of_team_chemistry
