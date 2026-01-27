class Solution(object):
    def firstUniqChar(self, s):
        hashmap = {}
        for x in s:
            hashmap[x] = hashmap.get(x , 0)+ 1
        for i in range(0, len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1

        
        
      
            

        """
        :type s: str
        :rtype: int
        """
        