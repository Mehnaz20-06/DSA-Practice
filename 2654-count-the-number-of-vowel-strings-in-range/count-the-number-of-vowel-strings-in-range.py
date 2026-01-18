class Solution(object):
    def vowelStrings(self, words, left, right): 
        vowel = {'a','e','i','o','u'}
        count = 0
        for i in range(left , right+1):
            word = words[i]
            if word[0] in vowel and word[-1] in vowel:
                count += 1
        return count


        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        