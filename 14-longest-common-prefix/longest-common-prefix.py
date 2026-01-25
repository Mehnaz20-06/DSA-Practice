class Solution(object):
    def longestCommonPrefix(self, strs):
        first= strs[0]
        n = len(first)
        prefix = []
        for i in range(n):
            char = first[i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return "".join(prefix)
            prefix.append(char)
        return "".join(prefix)
                    




       