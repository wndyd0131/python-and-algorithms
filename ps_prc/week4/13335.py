import sys
from collections import deque
queue = deque([])
answer = 0

def solution(w, L):
    global answer
    total = 0
    for i in range(len(arr)):
        if len(queue) == w: #큐가 꽉찼다면 비우기
            popped = queue.popleft()
            total -= popped
        while total + arr[i] > L:
            popped = queue.popleft()
            total -= popped
        if len(queue) == 0:
            queue.append(arr[i])
            total += arr[i]
            answer += w
        else:
            queue.append(arr[i])
            total += arr[i]
            answer += 1
    answer += 1

cmd = list(map(int, sys.stdin.readline().split()))
w = int(cmd[1])
L = int(cmd[2])
arr = list(map(int, sys.stdin.readline().split()))

solution(w, L)
print(answer)