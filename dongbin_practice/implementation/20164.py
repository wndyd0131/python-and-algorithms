import sys
import math
N = sys.stdin.readline().strip()

min_v = math.inf
max_v = 0

def countOdd(n):
    cnt = 0
    for i in n:
        if int(i) % 2 != 0:
            cnt += 1
    return cnt

def recursive(n, oddCount):
    global min_v, max_v

    if len(n) == 1:
        min_v = min(min_v, oddCount)
        max_v = max(max_v, oddCount)
    elif len(n) == 2:
        result = str(int(n[0]) + int(n[1]))
        recursive(result, oddCount + countOdd(result))
    else:
        for i in range(len(n)-2):
            for j in range(i+1, len(n)-1):
                result = str(int(n[:i+1]) + int(n[i+1:j+1]) + int(n[j+1:]))
                recursive(result, oddCount + countOdd(result))

recursive(N, countOdd(N))
print(min_v, max_v)