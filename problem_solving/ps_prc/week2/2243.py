import sys
N = int(sys.stdin.readline())
candyBox = dict()
for i in range(N):
    cmd = list(map(int, sys.stdin.readline().split()))
    if cmd[0] == 1:
        n = cmd[1]
        for key in sorted(candyBox.keys()):
            n -= candyBox[key]
            if n <= 0:
                print(key)
                candyBox[key] -= 1
                if candyBox[key] == 0:
                    del candyBox[key]
                break

    else:
        if cmd[1] in candyBox:
            candyBox[cmd[1]] += cmd[2]
        else:
            candyBox[cmd[1]] = cmd[2]