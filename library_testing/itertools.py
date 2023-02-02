# itertools
import itertools
from collections import Counter
dic = dict()
order = [2,3,4]
res = []
for o in order:
    for i in itertools.combinations("ABCDEFG", o):
        res.append(''.join(i))
        res.append('AC')
print(Counter(res).most_common())


# count() # 특정 숫자부터 카운트
# cycle() # 엘리먼트를 사이클링
# repeat() # 특정 숫자까지 반복

# accumulate() 쌓기, 즉 0부터 ~까지 합 과정 반환
# chain() 엘리먼트 묶기
# chain.from_iterable() 이터러블 묶기
# compress() [0,1] 리스트로 문자열 중 반환할 인덱스 선택하기
# takewhile(lambda, iterable) 조건식에 맞지 않을 때까지 sequence 반환
# dropwhile(lambda, iterable) 조건식에 맞지 않는 경우부터 sequence 반환 

# product() 카티션 프로덕트
# permutations() 순열
# combinations() 조합                                      ex) AB~
# combinations_with_replacement() 조합 (같은 원소도 조합에 포함) ex) AA~