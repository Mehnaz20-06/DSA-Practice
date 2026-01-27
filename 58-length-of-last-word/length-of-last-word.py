class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        s = s.split()
        word = s[-1]
        n = len(word)
        return n
        
        

        


        



        """
        :type s: str
        :rtype: int
        """
        