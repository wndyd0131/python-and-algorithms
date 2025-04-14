# 2215. Find the Difference of Two Arrays

# First Approach
class Solution:
    '''
    Approach:
        Initialization: 2 hash map
            - origDict: original frequency map of nums1
            - updatedDict: copy of origDict, used to detect change in origDict
        Loops:
            - Loop reversed till index 0
            - First loop:
                - check if nums2[i] already exists in updatedDict, if then increment and pop, otherwise just increment
                - resulting in distinct nums1
            - Second loop:
                - check if nums1[i] is different from updatedDict, if then increment and pop, otherwise just increment
                - resulting in distinct nums2

    Time Complexity: O(n+m)
    Space Complexity: O(n+m)
    '''
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # init
        origDict  = defaultdict(int)
        for i in nums1:
            origDict[i] += 1
        updatedDict = origDict.copy()

        for i in range(len(nums2) - 1, -1, -1):
            if updatedDict[nums2[i]] != 0:
                updatedDict[nums2[i]] += 1
                nums2.pop(i)
            else:
                updatedDict[nums2[i]] += 1
        for i in range(len(nums1) - 1, -1, -1):
            if origDict[nums1[i]] < updatedDict[nums1[i]]:
                updatedDict[nums1[i]] += 1
                nums1.pop(i)
            else:
                updatedDict[nums1[i]] += 1
        return [nums1, nums2]