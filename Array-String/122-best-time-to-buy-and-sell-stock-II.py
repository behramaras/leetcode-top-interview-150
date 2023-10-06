class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = prices[0]
        general_profit = 0

        for i in range(len(prices)):
            minimum = min(minimum, prices[i])
            if prices[i]-minimum > 0:
                general_profit += prices[i]-minimum
                minimum = prices[i]
        return general_profit
