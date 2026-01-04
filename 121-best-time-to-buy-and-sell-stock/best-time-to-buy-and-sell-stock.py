class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        bp = prices[0]
        for i in range(0,len(prices)):
            if prices[i] < bp:
                bp = prices[i]
            profit = prices[i] - bp
            maxProfit = max(maxProfit,profit)
        return maxProfit


        """
        :type prices: List[int]
        :rtype: int
        """
       

            