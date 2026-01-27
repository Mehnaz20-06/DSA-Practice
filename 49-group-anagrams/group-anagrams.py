class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            freq = [0]*26
            for i in range(0,len(s)):
                freq[ord(s[i]) - ord("a")] += 1

            res[tuple(freq)].append(s)
        return res.values()
        
        






        


     
        
        
        
        

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        