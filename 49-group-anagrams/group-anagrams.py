class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for i in range(0,len(s)):
                count[ord(s[i])  - ord("a")] += 1
                
            res[tuple(count)].append(s)
        return res.values()






        


     
        
        
        
        

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        