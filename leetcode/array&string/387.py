# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqmap = defaultdict(int)
        for val in s:
            freqmap[val] += 1
        for i, val in enumerate(s):
            if freqmap[val] == 1:
                return i
        return -1
    