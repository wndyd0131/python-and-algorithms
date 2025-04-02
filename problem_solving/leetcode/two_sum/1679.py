# 1679. Max Number of K-Sum Pairs

# Approach 1: Two Sum (filtering and sorting list)
def maxOperations(self, nums: List[int], k: int) -> int:
    """
     Time Complexity: O(nlogn)
     Space Complexity: O(n)
    """
    result = 0
    new_nums = []  # create new list
    for i in range(
            len(nums)):  # let new_nums only contain numbers that are smaller than k since larger numbers won't be used
        if nums[i] < k:
            new_nums.append(nums[i])
    new_nums.sort()  # sort in order to use two pointers
    i, j = 0, len(new_nums) - 1
    while i < j:
        if new_nums[i] + new_nums[j] == k:  # if sum == k, then move i to right, j to left, result++
            result += 1
            i += 1
            j -= 1
        elif new_nums[i] + new_nums[j] < k:  # if sum < k, then move i to right to sum with larger number
            i += 1
        else:  # if sum > k, then move j to left to sum with smaller number
            j -= 1
    return result