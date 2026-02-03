class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ans = []
        Kelvin = celsius + 273.15
        ans.append(Kelvin)
        Fahrenheit = celsius * 1.80 + 32.00
        ans.append(Fahrenheit)
        return ans
