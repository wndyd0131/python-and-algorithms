# 424. Longest Repeating Character Replacement

# Failed
    # The condition for expansion is wrong, should be while r < len(s)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Want to keep the most common alphabets in a window, therefore check if window contains replacable spot other than most common alphabets
        # Start sliding window from L, R = 0
        # Loop until L and R are both len(s) - 1
        # Record count of the alphabet
        # See if window size - most freq alphabet count <= k (meaning there's replacable spots)
            # if then, set window size as result after comparing with max
            # else, move L toward right
        # return result
        res = 0
        freqMap = {}
        l, r = 0, 0
        while l < len(s) or r < len(s):
            print(l, r)
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            mx = max(freqMap.values())
            w_size = r - l + 1
            if w_size - mx <= k:
                res = max(res, w_size)
            else:
                l += 1
                freqMap[s[r]] -= 1
            if r < len(s):
                r += 1
        return res