# 242. Valid Anagram

class Solution:
    '''
    Approach:
    0. validate count
    1. make two frequency maps: map1, map2
    2. count each alphabet of s and t, respectively
    3. iterate s or t, and compare key:value of map1 and map2
        - if equals, continue
        - else, return false

    Time complexity: O(s+t)
    Space complexity: O(s+t)

    Result: Success
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        freq_map1 = defaultdict(int)
        freq_map2 = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in s:
            freq_map1[i] += 1
        for i in t:
            freq_map2[i] += 1
        for i in s:
            if freq_map1[i] != freq_map2[i]:
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Approach:
        1. compare sum of ASCII

        Time Complexity: O(s+t)
        Space Complexity: O(1)

        Result: Fail
        Edge case:
            - different combinations can have equal sum
        '''
        sum1 = 0
        sum2 = 0
        for i in s:
            sum1 += ord(i)
        for i in t:
            sum2 += ord(i)
        if sum1 == sum2:
            return True
        else:
            return False