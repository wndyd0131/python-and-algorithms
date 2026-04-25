# 560. Subarray Sum Equals K
class Solution:
    '''
    Algorithms: Prefix Sum + Count
    Steps:
        1. nums [1,2,3,4,5]
        2. prefixSum [1,3,6,10,15]
        3. for i in range(nums)
            curSum += nums[i]
            targetSum = curSum - k
            if prefixSum map contains targetSum, then res += count of prefix
            resgister targetSum to prefixSum map

    Time complexity: O(N)
    Space complexity: O(N)
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumMap = {} # prefixSum: count
        prefixSumMap[0] = 1 # base case: for the case when curSum - k == 0, meaning sum is subarray itself instead of prefixSum
        curSum = 0
        res = 0
        for n in nums:
            curSum += n
            targetSum = curSum - k # if targetSum exists in prefixSum, that means subarray sum equals k
            if targetSum in prefixSumMap:
                res += prefixSumMap[targetSum]
            if curSum in prefixSumMap:
                prefixSumMap[curSum] += 1
            else:
                prefixSumMap[curSum] = 1
        return res