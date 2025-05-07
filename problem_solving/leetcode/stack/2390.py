# 2390. Removing Stars From a String

class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque([])
        for i in s:
            if i == "*":
                stack and stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)