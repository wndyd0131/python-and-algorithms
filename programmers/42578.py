# 의상
'''
https://school.programmers.co.kr/learn/courses/30/lessons/42578

# Hash map
# 경우의 수 문제
    # 경우의 수 (하나 선택한 경우 + 선택하지 않은 경우) - 예외 (모두 선택하지 않은 경우)
        # ex) 경우의 수 = a: (선택1 + 선택2 + 선택x) 곱하기 b: (선택1 + 선택x)
'''

def solution(clothes):
    ans = 1
    freqmap = {}
    for cloth in clothes:
        # 선택하지 않은 경우가 default로 들어가기 때문에 1로 시작
        freqmap[cloth[1]] = freqmap.setdefault(cloth[1], 1) + 1
    for k, v in freqmap.items():
        ans *= v
    return ans - 1