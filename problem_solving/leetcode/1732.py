# 1732. Find the Highest Altitude

class Solution:
    '''
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    def largestAltitude(self, gain: List[int]) -> int:
        cur, max_ = 0, 0
        for i in gain:
            cur += i
            max_ = max(cur, max_)
        return max_