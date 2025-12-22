class Solution(object):
    def groupAnagrams(self, strs):
        #Mehnaz
        #Optimal Solution = TC -> O(m x n)
        # m = length of strs
        # n = avg length of words in str
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a") ] += 1

            res[tuple(count)].append(s)
        return res.values()

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        