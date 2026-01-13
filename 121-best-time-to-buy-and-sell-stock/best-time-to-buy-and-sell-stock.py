class Solution(object):
    def maxProfit(self, prices):
        bp = prices[0]
        maxP = 0
        for i in range(len(prices)):
            if prices[i] < bp:
                bp = prices[i]
            profit = prices[i] - bp
            maxP = max(maxP,profit)
        return maxP
        
        

            

        


        """
        :type prices: List[int]
        :rtype: int
        """
       

            