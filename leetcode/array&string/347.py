# 347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums, k
        freqmap = dict()
        for num in nums:
            freqmap[num] = freqmap.setdefault(num, 0) + 1
        freqlist = sorted(freqmap.items(), key=lambda item:item[1])
        return [item[0] for item in freqlist[-1:-k-1:-1]]
        # edge cases


