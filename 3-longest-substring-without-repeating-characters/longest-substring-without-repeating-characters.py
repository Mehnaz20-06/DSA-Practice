class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        maxLen = 0
        left = 0
        for right in range(0,len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            maxLen = max(maxLen,right - left + 1)
        return maxLen


       
            

        """
        :type s: str
        :rtype: int
        """
        