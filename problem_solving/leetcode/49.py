# 49. Group Anagrams

class Solution:
    '''
    Approach
    1. iterate through the list
        - for each item, sort item 's' as 'sorted_s' then store 's' into hashMap['sorted_s']
    2. iterate through hashMap
        - append each value to the result

    Time complexity: O(nklgk), n = list, k = len(str)
    Space complexity: O(nk)
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashMap = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in hashMap:
                hashMap[sorted_s] = []
            hashMap[sorted_s].append(s)
        for i in hashMap:
            result.append(hashMap[i])
        return result