# retry
from functools import cmp_to_key
def solution(numbers):
    '''
    비교 정렬
    [3, 30, 34, 5, 9] 3vs30 (330vs.303)
    3앞
    [3,30,34,5,9] 30vs34 (3034vs3430)
    34앞 [3,34,30,5,9] 30vs5 (305vs530)
    5앞 [3,34,5,30,9] 30vs9 (309vs930)
    9앞 [3,34,5,9,30]
    이걸 더 반복하여 정렬
    
    파이썬 Comparator
    compare(a, b) < 0  # a가 b보다 앞에 와야 함
    compare(a, b) > 0  # b가 a보다 앞에 와야 함
    compare(a, b) == 0 # 순서 상관없음
    
    1. 문자열 리스트로 변환
    2. 비교 정렬
    
    key takeaways
    1. 비교 정렬
    2. key=cmp_to_key(compare)
        - Python3에서는 정렬의 key로 comparator를 못 넣기 때문에, functools의 cmp_to_key를 사용 
    '''
    answer = ''
    nums = list(map(str, numbers))
    
    def compare(a, b):
        if a + b < b + a:
            return 1
        elif b + a < a + b:
            return -1
        else:
            return 0
    
    nums.sort(key=cmp_to_key(compare))
    answer = ''.join(nums)
    return '0' if answer[0] == '0' else answer # if 000 then 0