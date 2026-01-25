class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        s = s.split()
        n = len(s)
        words = []
        for i in range(n-1,-1,-1):
            words.append(s[i])
        return " ".join(words)

        
      
       
        