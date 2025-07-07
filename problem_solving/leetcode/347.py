# 347. Top K Frequent Elements

from collections import defaultdict

class Solution:
    '''
    Approach: Built-in sort
    Time complexity: O(n + mlgm) = O(nlgn)
    Space complexity: O(m + k) = O(n)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freqMap = defaultdict(int)
        for i in nums:
            freqMap[i] += 1
        sorted_map = sorted(freqMap.items(), key=lambda kv: (kv[1], kv[0]))
        for i in range(-1, -k-1, -1):
            result.append(sorted_map[i][0])
        # or result.extend([pair[0] for pair in sorted_map[-1:-k-1:-1]])
        return result

import heapq

class Solution:
    '''
    Approach: Heap sort
    Time complexity: O(n + klgm) = O(nlgn)
    Space complexity: O(n + k) = O(n)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        freqMap = defaultdict(int)
        for i in nums:
            freqMap[i] += 1
        for kv in freqMap.items():
            heapq.heappush(heap, (-kv[1], kv[0]))
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

class Solution:
    '''
    Approach: Bucket sort
        - Count sort uses [idx][count]
        - Bucket sort uses [count][number list]
    Time complexity: O(n)
    Space complexity: O(n + k) = O(n)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        bucket = [[] for _ in range(len(nums) + 1)]
        freqMap = defaultdict(int)
        for i in nums:
            freqMap[i] += 1

        for i in freqMap:
            idx = freqMap[i]
            bucket[idx].append(i)
        for i in range(len(bucket) - 1, -1, -1):
            for j in bucket[i]:
                result.append(j)
                if (len(result) == k):
                    return result
        return result