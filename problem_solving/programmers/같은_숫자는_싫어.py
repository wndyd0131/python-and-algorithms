def solution(arr): # range 0-9
    answer = []
    target = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != target:
            answer.append(arr[i])
        target = arr[i]
    return answer[::-1]
  
# Tracking last element
def solution(arr): # range 0-9
    answer = []
    for num in arr:
        if not answer or answer[-1] != num:
            answer.append(num)
    return answer