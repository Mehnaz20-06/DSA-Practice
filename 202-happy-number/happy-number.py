class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.happyNum(n)
        return n == 1
    def happyNum(self, n):
        total = 0
        while n != 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    



        