import sys
N = int(sys.stdin.readline().strip())
route = sys.stdin.readline().split()
result = [1, 1]
for i in route:
    if i == 'L':
        if result[1] != 1:
            result[1] += -1
        else:
            continue
    elif i == 'R':
        if result[1] != N:
            result[1] += 1
        else:
            continue
    elif i == 'U':
        if result[0] != 1:
            result[0] += -1
        else:
            continue
    else:
        if result[0] != N:
            result[0] += 1
print(result[0], result[1])