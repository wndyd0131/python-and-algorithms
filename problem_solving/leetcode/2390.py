# 2390. Removing Stars From a String

# First Approach
class Solution:
    '''
    Approach:
        1. Append to list when it's not '*'
        2. Pop when it's '*'

    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def removeStars(self, s: str) -> str:
        stack = deque([])
        for i in s:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)

# Second Approach
class Solution:
    '''
    Approach:
        Same as before

    Change:
        Consider empty stack

    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def removeStars(self, s: str) -> str:
        stack = deque([])
        for i in s:
            if i == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)