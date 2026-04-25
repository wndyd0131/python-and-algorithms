# 981. Time Based Key-Value Store
class TimeMap:
    '''
    Algorithms: Brute Force
    '''
    def __init__(self):
        # key, value, timestamp
        # foo, bar, 1
        # key+timestamp
        # key [{timestamp, value}]
        self.timeMap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        '''
        store to key (value, timestamp)
        [1,2,5,8,15,40,100,120]
        110
        binary search
        if value <= target:
            save
        else:
            continue
        '''
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        '''
        if exists, return previously set key with the closest timestamp
        if not exists, return ""
        '''
        val = ""
        if key in self.timeMap:
            for k in self.timeMap[key]:
                if k[0] <= timestamp:
                    val = k[1]
                else:
                    break
            return val
        else:
            return ""

class TimeMap:
    '''
    Algorithms: Binary Search
    '''
    def __init__(self):
        # key, value, timestamp
        # foo, bar, 1
        # key+timestamp
        # key [{timestamp, value}]
        self.timeMap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        '''
        store to key (value, timestamp)
        [1,2,5,8,15,40,100,120]
        110
        binary search
        if value <= target:
            save
        else:
            continue
        '''
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        '''
        if exists, return previously set key with the closest timestamp
        if not exists, return ""
        '''
        val = ""
        if key in self.timeMap:
            l = 0
            r = len(self.timeMap[key]) - 1
            while l <= r:
                mid = (l + r) // 2
                curTime = self.timeMap[key][mid][0]
                curVal = self.timeMap[key][mid][1]
                if curTime == timestamp:
                    return curVal
                if curTime < timestamp:
                    l = mid + 1
                    val = curVal
                else:
                    r = mid - 1
        return val


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Cleaner Version
class TimeMap:

    def __init__(self):
        # key, value, timestamp
        # foo, bar, 1
        # key+timestamp
        # key [{timestamp, value}]
        self.timeMap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        '''
        store to key (value, timestamp)
        [1,2,5,8,15,40,100,120]
        110
        binary search
        if value <= target:
            save
        else:
            continue
        '''
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        '''
        if exists, return previously set key with the closest timestamp
        if not exists, return ""
        '''
        val = ""
        values = self.timeMap.get(key, [])
        if values:
            l, r = 0, len(values) - 1
            while l <= r:
                mid = (l + r) // 2
                curTime = values[mid][0]
                curVal = values[mid][1]
                if curTime == timestamp:
                    return curVal
                if curTime < timestamp:
                    l = mid + 1
                    val = curVal
                else:
                    r = mid - 1
        return val


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)