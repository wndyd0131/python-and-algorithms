# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        shortest_idx = 0
        # Get shortest string from strs
        for i, s in enumerate(strs):
            if len(strs[shortest_idx]) > len(s):
                shortest_idx = i
        shortest_str = strs[shortest_idx]
        # Compare character one by one
        for i in range(len(shortest_str)):
            for s in strs:
                if s[i] != shortest_str[i]:
                    return result
            result = shortest_str[:i+1]
        return result