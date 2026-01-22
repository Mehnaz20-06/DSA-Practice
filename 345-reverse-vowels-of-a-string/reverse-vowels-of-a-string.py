class Solution(object):
    def reverseVowels(self, s):
        #Strings are immutable
        #We convert String to list
        s = list(s)
        left = 0
        n = len(s)
        right = n -1
        vowels = ('aeiouAEIOU')
        while left < right:
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
            if s[left] in vowels and s[right] in vowels:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
        return "".join(s)
            
            



        """
        :type s: str
        :rtype: str
        """
        