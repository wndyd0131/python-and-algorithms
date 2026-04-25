class Solution:
    '''
    Algorithms: Sliding window
        Step:
            # create freqMap for s1
            # l = 0
            # r starting from len(s1) - 1, repeat until r len(s2) (loop)
                # create freqMap for s2
                # matches = 0
                # compare each values (loop)
                    # if exists in s1
                        # then, if count equals
                            # then count++
                            # else break
                    # else
                        # break
                # if matches == len(freqMap)
                    # return True
                # else
                    # continue
            # return False
    Time complexity: O(s1 * s2) = O(N * K)
    Space complexity: O(26) = O(1)
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freqMap1 = {}
        for s in s1:
            freqMap1[s] = freqMap1.get(s, 0) + 1
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            freqMap2 = {}
            for s in s2[l:r+1]:
                freqMap2[s] = freqMap2.get(s, 0) + 1
            matches = 0
            for k, v in freqMap1.items():
                if k in freqMap2 and freqMap1[k] == freqMap2[k]:
                    matches += 1
                else:
                    break
            if matches == len(freqMap1):
                return True
            l += 1
        return False


class Solution:
    '''
    Algorithms: Sliding window
        Step:
            # Same as above
                # Above code unnecessarily recomputes every element again, leading to K times computation
                # It can be optimized by reusing the window by removing first item and adding last item as window moves
    Time complexity: O(26N)
    Space complexity: O(26) = O(1)
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqMap1 = {}
        freqMap2 = {}
        for s in s1:
            freqMap1[s] = freqMap1.get(s, 0) + 1
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            if r == len(s1) - 1:
                for s in s2[l:r+1]:
                    freqMap2[s] = freqMap2.get(s, 0) + 1
            else:
                freqMap2[s2[r]] = freqMap2.get(s2[r], 0) + 1
            matches = 0
            for k, v in freqMap1.items():
                if k in freqMap2 and freqMap1[k] == freqMap2[k]:
                    matches += 1
                else:
                    break
            if matches == len(freqMap1):
                return True
            freqMap2[s2[l]] -= 1
            l += 1
        return False