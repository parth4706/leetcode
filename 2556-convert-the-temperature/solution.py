class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [float(celsius+273.15),float(celsius*1.80+32.00)]
