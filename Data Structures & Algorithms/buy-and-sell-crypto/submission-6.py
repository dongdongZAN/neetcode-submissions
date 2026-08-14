class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # res = 0
        # start, end = 0, 1
        # for i in range(len(prices) - 1):
        #     start = i
        #     while start < len(prices)-1 and prices[start] >= prices[start+1]:
        #         start += 1
        #     end = start + 1
        #     while end < len(prices) and prices[end] >= prices[start]:
        #         res = max(res, prices[end]-prices[start])
        #         end += 1
             
        # return res



        # maxP = 0

        # minBuy = prices[0]
        # for sell in prices:
        #     maxP = max(maxP, sell - minBuy)
        #     minBuy = min(minBuy, sell)
        # return maxP



        maxP = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right += 1
        return maxP
