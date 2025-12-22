class Solution(object):
    def largestAltitude(self, gain):
        #Mehnaz
        current = 0
        max_gain = 0
        for g in gain:
            current += g
            max_gain = max(max_gain,current)
        return max_gain
        

        """
        :type gain: List[int]
        :rtype: int
        """
        