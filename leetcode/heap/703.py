# 703. Kth Largest Element in a Stream

class KthLargest:
    '''
    Algorithms: Heap
    Status: Failed
    Problem: nlargest copy whole n size heap and pop until kth largest
    Time complexity: O(N log K)
    Space complexity: O(N)
    '''
    def __init__(self, k: int, nums: List[int]):
        # k = 5
        # nums = [4,5,8,2]
        self.scores = nums
        self.k = k
        heapq.heapify(self.scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.scores, val)
        maxi = heapq.nlargest(self.k, self.scores)
        return maxi[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

class KthLargest:
    '''
    Algorithms: Heap
    Status: Success
    Optimization: Limit heap size to k, so that kth largest can be accessed through index[0]
    Time complexity: O(log K)
    Space complexity: O(K)
    '''
    def __init__(self, k: int, nums: List[int]):
        # k = 5
        # nums = [4,5,8,2]
        self.scores = nums
        self.k = k
        heapq.heapify(self.scores)
        while len(self.scores) > k:
            heapq.heappop(self.scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.scores, val)
        if len(self.scores) > self.k:
            heapq.heappop(self.scores)
        return self.scores[0]