# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        L M R
        By splitting into left and right splits, we can compute with sorted array either with left or right one
        1. if L <= M: then left, else right
        2. if left, then check L <= target <= M, else check M <= target <= R
        3. if L <= target <= M, then move mid to left, else move to right
        '''
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1