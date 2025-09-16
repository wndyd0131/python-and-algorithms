class Solution: # Memory Limit
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
          starting from mid
            assume k = mid, compute (using division and mod operation), test if result == target
            try eating all the bananas by looping -> count the loop -> if count == h then return mid
                - divide by numbers and if mod > 0 then + 1
                -> if count > h then too slow so left = mid + 1, if count < h then too fast so right = mid - 1

        Problems:
          1. Memory Limit Exceeded since list is created depending on max value of the input. If max value is 10^9, then 10^9 spaces should be assigned.
          2. Wrong Solution, total ≤ h provides all possible solution, therefore minimum k should be chosen from all those solutions

        Time Complexity: O(log(max(piles)) * len(piles))
        Space Complexity: O(max(piles))
        '''
        ks = [i for i in range(1, max(piles)+1)]
        l = 0
        r = len(ks) - 1
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for pile in piles:
                val = pile // ks[mid]
                rem = pile % ks[mid]
                total += val
                if rem > 0:
                    total += 1
            print(ks[mid], mid, total)
            if total == h:
                return ks[mid]
            elif total > h:
                l = mid + 1
            elif total < h:
                r = mid - 1
            print("L",l,"R",r)
        return 0
    

class Solution: # Correct Solution
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Algorithm:
          starting from mid
            assume k = mid, compute (using division and mod operation), test if result == target
            try eating all the bananas by looping -> count the loop -> if count == h then return mid
                - divide by numbers and if mod > 0 then + 1
                -> if count > h then too slow so left = mid + 1, if count <= h then too fast so right = mid - 1
        Time Complexity: O(log(max(piles)) * len(piles))
        Space Complexity: O(1)
        '''
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

class Solution: # Optimized Solution (faster due to math.ceil())
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Algorithm:
          starting from mid
            assume k = mid, compute (using math.ceil()), test if result == target
            try eating all the bananas by looping -> count the loop -> if count == h then return mid
                - divide by numbers and if mod > 0 then + 1
                -> if count > h then too slow so left = mid + 1, if count <= h then too fast so right = mid - 1
        Time Complexity: O(log(max(piles)) * len(piles))
        Space Complexity: O(1)
        '''
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res