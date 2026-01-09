class Solution(object):
    def countPrimes(self, n):
        #Mehnaz
        #Edge case
        if n < 2:
            return 0
        #creating a boolean array first uptil n 
        isPrime = [True] * n
        # marking 0 and 1 as NON PRIME
        isPrime[0] = isPrime[1] = False
        # each number from 2 up to √n
        for i in range(2,int(n**0.5)+1):
            if isPrime[i]:
                for j in range(i*i , n , i):
                    isPrime[j] = False


        return sum(isPrime)


        
       