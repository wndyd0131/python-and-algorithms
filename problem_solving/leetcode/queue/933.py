# 933. Number of Recent Calls

from collections import deque

class RecentCounter:

    def __init__(self):
        self.request_q = deque([])

    def ping(self, t: int) -> int:
        self.request_q.append(t)
        while self.request_q and self.request_q[0] < t - 3000:
            self.request_q.popleft()
        return len(self.request_q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)