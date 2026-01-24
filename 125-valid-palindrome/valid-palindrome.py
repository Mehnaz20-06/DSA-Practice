class Solution(object):
    def isPalindrome(self, s):
        s = s.strip()
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        n = len(s)
        left = 0
        right = n-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
   
    
     
        """
        :type s: str
        :rtype: bool
        """
   
    