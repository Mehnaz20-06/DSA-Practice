class Solution(object):
    def longestCommonPrefix(self, strs):
        #Mehnaz
        #Solution using min and max
        if not strs:
            return ""
        smallest = min(strs)
        largest = max(strs)
        for i in range(0,len(smallest)):
            if smallest[i] != largest[i]:
                return smallest[:i]
        return smallest        

        
        """
        :type strs: List[str]
        :rtype: str
        """
        