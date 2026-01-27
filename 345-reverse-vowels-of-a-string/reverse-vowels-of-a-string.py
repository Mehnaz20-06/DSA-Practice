class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        vowels = set("aeiouAEIOU")
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[right] , s[left] = s[left] , s[right]
                left += 1
                right -= 1
            elif s[left] in vowels:
                right -= 1
            else:
                left += 1
        return "".join(s)
        
               