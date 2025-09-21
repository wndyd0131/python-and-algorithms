class Solution:
    # if brute force O(n^2)
    # can optimize to O(n)
    '''
    Algorithm: (Sliding Window using two pointers)
    1. if length < 2, return 0
    2. starting from idx 0, setting x to 0, y to 1
        while y < len
            if x <= y, then y - x, then compare with max_profit
            if x > y, move x to y
    3. return max_profit
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        i = 0
        profit = 0
        for j in range(1, len(prices)):
            if prices[i] <= prices[j]:
                profit = max(profit, prices[j] - prices[i])
            else:
                i = j
        return profit

class Solution:
    '''
    Another Solution without using two pointers
    '''
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update buy price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit  # Update max profit

        return max_profit