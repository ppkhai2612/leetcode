class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s, f = 0, 1 # two pointers
        max_profit = 0

        while f < len(prices): # O(n)
            # Profit to sell on this day
            # update biggest profit
            if prices[s] < prices[f]:
                cur_profit = prices[f] - prices[s]
                max_profit = max(cur_profit, max_profit)
            # Whenever we encounter a lower price, we “forget” all the previous buy days, because they cannot generate any higher profits
            else:
                s = f
            
            f += 1

        return max_profit