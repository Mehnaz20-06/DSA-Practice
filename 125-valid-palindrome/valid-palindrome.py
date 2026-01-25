class Solution(object):
    def isPalindrome(self, s):
        s = s.strip()
        s = s.lower()
        s = "".join(char for char in s if char .isalnum())
        left = 0
        n = len(s)
        right = n - 1
        while left < right :
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
       
        """
        :type s: str
        :rtype: bool
        """
   
    