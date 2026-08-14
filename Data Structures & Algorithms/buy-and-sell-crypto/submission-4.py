class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        start, end = 0, 1
        for i in range(len(prices) - 1):
            start = i
            print(start)
            while start < len(prices)-1 and prices[start] >= prices[start+1]:
                start += 1
            end = start + 1
            print(start, end)
            while end < len(prices) and prices[end] >= prices[start]:
                res = max(res, prices[end]-prices[start])
                end += 1

            
             
        return res