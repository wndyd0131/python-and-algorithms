# Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = list(s)
        str2 = list(t)
        str1 = "".join(sorted(str1))
        str2 = "".join(sorted(str2))
        return str1 == str2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)
        for c in s:
            hashmap1[c] += 1
        for c in t:
            hashmap2[c] += 1
        
        return hashmap1 == hashmap2
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        for val in s:
            hashmap[val] += 1
        for val in t:
            hashmap[val] -= 1
        for k, v in hashmap.items():
            if v != 0:
                return False
        return True