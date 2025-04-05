# 643. Maximum Average Subarray I

# First Approach (Brute Force)
class Solution:
    '''
    Approach:
    Slide through nums with k window from [0] to the possible end
    and for each iteration sum up all the k elements

    Time Complexity: O(nk)

    Space Complexity: O(k)
    '''
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ = -float('inf')
        for i in range(len(nums) - (k-1)):
            sum_ = sum(nums[i:i+k])
            max_ = max(sum_, max_)
        return max_ / k

# Second Approach
class Solution:
    '''
    Approach:
    For each iteration, elements other than nums[i - k] and nums[i] remain unchanged,
    subtract the first element [i - k] and add the upcoming element [i]
    to avoid redundant computation.

    Time Complexity: O(n)

    Space Complexity: O(1)
    '''
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ = sum(nums[:k])
        if len(nums) > 1:
            cur_sum = sum(nums[1:k])
            for i in range(1, len(nums) - (k-1)):
                cur_sum += nums[i+(k-1)]
                max_ = max(cur_sum, max_)
                cur_sum -= nums[i]
        return max_ / k

# Second Approach - Cleaner code
def findMaxAverage(self, nums: List[int], k: int) -> float:
    cur_sum = sum(nums[:k])
    max_ = cur_sum
    for i in range(k, len(nums)):
        cur_sum += nums[i] - nums[i - k]
        max_ = max(max_, cur_sum)
    return max_ / k