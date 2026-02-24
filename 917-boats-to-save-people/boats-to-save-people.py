class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # sort the people
        people.sort()

        boat_number = 0

        
        left = 0
        right = len(people) - 1
        number_of_people_on_boats = 0
        while left < right:
            if people[left] + people[right] <= limit:
                boat_number+=1
                left+=1
                right-=1
                number_of_people_on_boats+=2
            else:
                boat_number+=1
                right-=1
                number_of_people_on_boats+= 1
        
        if number_of_people_on_boats != len(people):
            boat_number+=1
        return boat_number

        