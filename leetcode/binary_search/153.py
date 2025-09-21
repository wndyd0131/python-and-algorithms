class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Algorithm
        1. if sorted (l < r), either cur_min or first element is minimum
        2. else
            - if mid >= left, min is somewhere at right
            - if mid < left, min is somewhere at left
        Time Complexity: O(log n)
        Space Complexity: O(1)
        '''

        l = 0
        r = len(nums) - 1
        cur_min = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                return min(cur_min, nums[l])
            m = (l + r) // 2
            cur_min = min(cur_min, nums[m])
            if nums[m] >= nums[l]: # right portion has minimum
                l = m + 1
            else: # left portion has minimum
                r = m - 1
        return cur_min