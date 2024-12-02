import sys

dp = [0] * 1001

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
mx = max(arr)
result = list()
for i in range(N):
    res = max(dp[1:arr[i]])
    if res == 0:
        dp[arr[i]] = 1
    else:
        dp[arr[i]] = res + 1
print(max(dp))

# trial 1:  잘못 구현함: 수열에 대한 정보를 저장히자 못해서 숫자만 출력 가능



# 최고의 경우에는 O(N)으로 해결 될 수 있는 문제
    # 잘 정렬이 되어 있는 경우
# 최악의 경우
    # 반대로 정렬이 되어 있는 경우 또는 랜덤한 경우

# 80 100 90 150 95 160 96 97 170 98 130
# 이러한 데이터가 있는 경우 130에서 100을 다시 접근해야 함

'''
DP:
- 큰 문제를 작은 문제로 나눌 수 있음
- 동일한 작은 문제가 반복됨
- 캐싱 (DP 테이블에 저장하고, 필요 시 사용)
- 상향식 작 -> 큰: 반복문
- 하향식 큰 -> 작: 재귀
- 점화식 세우기 ai
'''