class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        s = s.split()
        left = 0
        n = len(s)
        right  = n - 1
        while left < right:
            s[left] , s[right] = s[right],s[left]
            left += 1
            right -= 1
        return " ".join(s)
        
        