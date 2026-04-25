class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if str[i] exists in hashmap
            # then cut off the latest duplicate character
                # cur_max = str[i] - hashmap[str[i]], then plus current one -> cur_max += 1
            # then compare max(res, cur_max)
            # initialize hashmap
        # if not, then add character to hashmap and cur_max += 1
        hashmap = {}
        res = 0
        cur = 0
        for i in range(len(s)):
            if s[i] in hashmap:
                res = max(res, cur)
                cur = i - hashmap[s[i]]
                start = hashmap[s[i]] + 1
                hashmap = {}
                for j in range(start, i+1):
                    hashmap[s[j]] = j
            else:
                cur += 1
            hashmap[s[i]] = i
        return max(res, cur)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if str[i] exists in hashmap
        # then cut off the latest duplicate character
        # cur_max = str[i] - hashmap[str[i]], then plus current one -> cur_max += 1
        # then compare max(res, cur_max)
        # initialize hashmap
        # if not, then add character to hashmap and cur_max += 1
        char_set = set()
        res = 0
        cur = 0
        i = 0
        for j in range(len(s)):
            if s[j] in char_set:
                while s[i] != s[j]:
                    char_set.remove(s[i])
                    i += 1
                i += 1
                cur = j - i
            else:
                char_set.add(s[j])
            cur += 1
            res = max(res, cur)
        return res

class Solution: # Optimized version
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if str[i] exists in hashmap
            # then cut off the latest duplicate character
                # cur_max = str[i] - hashmap[str[i]], then plus current one -> cur_max += 1
            # then compare max(res, cur_max)
            # initialize hashmap
        # if not, then add character to hashmap and cur_max += 1
        char_set = set()
        res = 0
        i = 0
        for j in range(len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            char_set.add(s[j])
            res = max(res, j - i + 1)
        return res

