# from sys import stdin, stdout
# input = stdin.readline
# printStr = stdin.write

### 각 변수에 할당받기
# a = '4 5 6'
# a, b, c = map(int, a.split())
# print(a)

### 2차원 배열 받기
# MAP = [list(map(int, input().split())) for _ in range(int(input()))]
# print(MAP)

### N 이후로 입력받는 값들은 arr이 배열로 받음
# N, *arr = map(int, input().split())

### 문자열 각 문자 배열에 받기
# arr = [list(input().strip()) for _ in range(int(input()))]
# print(arr)

### 배열 문자열로 붙이기
# arr = [1,2,3,4]
# print("".join(map(str, arr)))

### 배열 띄어서 출력하기
# arr = [1,2,3,4]
# print(*arr)

### 재귀함수의 recursion depth의 제한을 완화하는 함수
# setrecursionlimit()

from collections import Counter
nums = [9,4,1,7,8,1,3,6,5,2]
counter = Counter(nums)
print(counter)