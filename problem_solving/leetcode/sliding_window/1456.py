# 1456. Maximum Number of Vowels in a Substring of Given Length

# First Approach
class Solution:
    '''
    Approach:
    1) Initialize hashmap with first k substrings
    2) Set cur_sum with sum of keys 'a','e','i','o','u', and set it as max
    3) for k to the end of string, subtract key of 'left-end' and add 'right-end' since only those two are changing values
    4) Try sum of keys 'a','e','i','o','u' again and compare with max

    Time Complexity: O(n)
    Space Complexity: O(1), since it's bounded by alphabet size
    '''
    def maxVowels(self, s: str, k: int) -> int:
        d = defaultdict(int)
        for i in range(k):
            d[s[i]] += 1
        cur_sum = d['a'] + d['e'] + d['i'] + d['o'] + d['u']
        max_ = cur_sum
        for i in range(k, len(s)):
            d[s[i-k]] -= 1
            d[s[i]] += 1
            cur_sum = d['a'] + d['e'] + d['i'] + d['o'] + d['u']
            max_ = max(max_, cur_sum)
        return max_