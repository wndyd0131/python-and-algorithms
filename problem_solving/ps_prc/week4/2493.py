import sys
N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

max_index = [0,-1]
stack = []
answer = []

def solution(arr):
    if max_index[1] == -1:
        stack.append(0)
        max_index[0], max_index[1] = arr[0], 0

    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            stack.append(i+1)
        else:
            if max_index[0] > arr[i+1]:
                stack.append(max_index[1]+1)
            # elif max_index[0] == arr[i+1]:
            #     stack.append(max_index[1]+1)
            #     max_index[1] = i+1
            else:
                stack.append(0)
                max_index[0], max_index[1] = arr[i+1], i+1


solution(arr)
for i in range(len(stack)):
    if i == len(stack)-1:
        break
    print(stack[i], end = " ")

print(stack[len(stack)-1])