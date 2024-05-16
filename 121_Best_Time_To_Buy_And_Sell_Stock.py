class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1
        while left < right and right < len(prices):
            current_profit = prices[right] - prices[left]
            if current_profit > 0:
                max_profit = max(max_profit, current_profit)
            if prices[right] <= prices[left]:
                left = right
                right += 1
            elif right == len(prices) - 1:
                left += 1
                right = left + 1
            else:
                right += 1
        return max_profit
