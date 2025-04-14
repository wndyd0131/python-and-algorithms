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

# Second Approach
class Solution:
    '''
    Approach:
        Same as before, but using set() to remove duplicate beforehand instead of removing during loop
    Time Complexity: O(n+m)
    Space Complexity: O(n+m)
    '''
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # init
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        freqMap = defaultdict(int)
        for i in nums1: # initializing freqMap for nums1
            freqMap[i] += 1

        for i in range(len(nums2) - 1, -1, -1): # initializing freqMap for nums2 + updating  freqMap for nums1
            freqMap[nums2[i]] += 1
            if freqMap[nums2[i]] > 1:
                nums2.pop(i)
        for i in range(len(nums1) - 1, -1, -1):
            if freqMap[nums1[i]] > 1:
                nums1.pop(i)
        return [nums1, nums2]


# Third Approach
class Solution:
    '''
    Approach
        1. Remove duplicate inside nums1 and nums2
        2. Check if nums1[i] is not in nums2, if then append to new list, otherwise remove from nums2
        3. Return new list and nums2
    Time Complexity: O(n+m)
    Space Complexity: O(n+m)

    Faster Approach :)
        - Using set allowing O(1) for comparison and removal
    '''
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans1 = []
        for num in nums1:
            if num not in nums2: #O(1)
                ans1.append(num)
            else:
                nums2.remove(num) #O(1)
        return [ans1, list(nums2)] # O(m) due to conversion