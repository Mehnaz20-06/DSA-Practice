class Solution(object):
    def countVowelSubstrings(self, word):
        n = len(word)
        vowels = "aeiou"
        count  = 0
        for i in range(0,n):
            seen = set()

            for j in range(i , n):
                if word[j] not in vowels:
                    break
                seen.add(word[j])
                if len(seen) == 5:
                    count += 1
        return count
                






      