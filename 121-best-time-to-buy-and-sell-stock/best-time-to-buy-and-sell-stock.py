class Solution(object):
    def maxProfit(self, prices):
        bp = prices[0]
        maxProfit = 0
        n = len(prices)
        for i in range(0,n):
            if prices[i] < bp:
                bp = prices[i]
            profit = prices[i] - bp
            maxProfit = max(profit , maxProfit)
        return maxProfit
        


        


        """
        :type prices: List[int]
        :rtype: int
        """
       

            