# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freqmap = defaultdict(int)
        res = ""
        for c in s:
            freqmap[c] += 1
        for c in t:
            freqmap[c] -= 1
        for k, v in freqmap.items():
            if v < 0:
                res = k
        return res

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for char in t:
            result += ord(char)
        for char in s:
            result -= ord(char)
        return chr(result)