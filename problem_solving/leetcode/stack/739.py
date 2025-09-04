class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Algorithm: Stack, pop with relative number of day passed
        # 1. for idx, i in enumerate(temperatures)
            # if len(stack) > 0, then compare temperature at top vs. i while stack has an element and i > top
                # if i > top, then pop top and update corresponding index with relative day (= cur_idx - index)
            # push (temperature[i], index)
        # 2. return answer

        # Time complexity: O(n)
        # Space complexity: O(n)
        '''

        answer = [0] * len(temperatures)
        stack = []
        for cur_day, cur_temperature in enumerate(temperatures):
            while stack and cur_temperature > stack[-1][0]:
                _, day = stack.pop()
                answer[day] = cur_day - day
            stack.append((cur_temperature, cur_day))
        return answer

class Solution:
    '''
    Optimized Version:
        # Slightly faster due to use of primitive type instead of tuple, reducing overhead of generating and accessing tuple object
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        return answer