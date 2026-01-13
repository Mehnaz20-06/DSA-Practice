class Solution(object):
    def reverseWords(self, s):
        words = s.strip().split()
        res = ""
        n = len(words)
        for i in range (n-1,-1,-1):
            if i != 0:
                res += words[i] + " "
            else:
                res += words[i]  
        return res
        """
        :type s: str
        :rtype: str
        """
        