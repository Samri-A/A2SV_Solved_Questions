class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 360/60 = 6
        # 180 - 30
        # 360/12 = 30
        # 15 - 12:30
        # 30/60 = 0.5 => 15

        hour_angle = (30 * (hour%12)) + (minutes*0.5)
        minutes_angle = 6 * minutes


        # print(hour_angle) 
        # print(minutes_angle)
        
        val = abs( minutes_angle - hour_angle)
        return  val if (360 - val) > val else 360-val
