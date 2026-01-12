class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        j = n -1
        i = 0
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i+1, j+1]
            elif total < target:
                i += 1
            elif total > target:
                j -= 1
            else:
                return []
                
        
            
        
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        