# 1679. Max Number of K-Sum Pairs

# Approach 1: Two Sum (sorted list)
def maxOperations(self, nums: List[int], k: int) -> int:
    """
     Time Complexity: O(nlogn)
     Space Complexity: O(1)
    """
    result = 0
    nums.sort()  # sort in order to use two pointers
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == k:  # if sum == k, then move i to right, j to left, result++
            result += 1
            i += 1
            j -= 1
        elif nums[i] + nums[j] < k:  # if sum < k, then move i to right to sum with larger number
            i += 1
        else:  # if sum > k, then move j to left to sum with smaller number
            j -= 1
    return result