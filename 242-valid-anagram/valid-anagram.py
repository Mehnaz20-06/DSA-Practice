class Solution(object):
    def isAnagram(self, s, t):
        #Mehnaz
        if len(s) != len(t):
            return False
        freq = [0]*26
        for i in range(0,len(s)):
            freq[ord(s[i]) - ord("a")] += 1
            freq[ord(t[i]) - ord("a")] -= 1
        for x in freq:
            if x != 0:
                return False
        return True

       