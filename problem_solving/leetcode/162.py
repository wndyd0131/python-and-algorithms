# 162. Find Peak Element

class Solution:
    # Input
    # list of numbers

    # Output
    # any single index that is peak

    # Consider
    # left boundary and right boundary are both -inf
    # Choosing greater from mid-1 and mid+1 gives the result eventually since both boundaries have smaller values

    # Algorithm
    # 1. initialize left, right, and mid
    # 2. if mid == 0 or n - 1
    # 2-1. if mid == 0, mid > right then mid else right
    # 2-2. if mid == n-1, mid > left then mid else left
    # 3. if mid > left and mid > right, then return mid
    # 4. else if left > mid, then mid = left + (mid - 1) // 2
    # 5. else if right > mid, then mid = right + (mid + 1) // 2

    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                return mid if nums[mid] > nums[right] else right
            elif mid == len(nums) - 1:
                return mid if nums[mid] > nums[left] else left
            else:
                if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    if nums[mid - 1] > nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
