import sys
time = 0
def solution(w, L):
    global time
    bridge = [0] * w
    while bridge:
        time += 1
        bridge.pop(0)
        if arr:
            if sum(bridge) + arr[0] <= L:
                bridge.append(arr.pop(0))
            else:
                bridge.append(0)

cmd = list(map(int, sys.stdin.readline().split()))
w = int(cmd[1])
L = int(cmd[2])
arr = list(map(int, sys.stdin.readline().split()))

solution(w, L)
print(time)