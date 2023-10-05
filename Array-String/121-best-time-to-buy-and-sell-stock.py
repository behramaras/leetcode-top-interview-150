class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        minimum = prices[0]

        for i in range(len(prices)):
            minimum = min(minimum, prices[i])
            max_profit = max(max_profit, prices[i] - minimum)
        return max_profit
