# 1624. Largest Substring Between Two Equal Characters

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dp = [None] * 101
        mx = 0
        empty = 1
        for i in range(len(s)):
            if dp[ord(s[i]) - 96] == None:
                dp[ord(s[i]) - 96] = i
            else:
                empty = 0
                diff = abs(dp[ord(s[i]) - 96] - i) - 1
                if mx < diff:
                    print(s[i])
                    mx = diff
        if empty:
            return -1
        else:
            return mx