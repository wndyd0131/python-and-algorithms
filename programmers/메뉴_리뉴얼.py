import itertools
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for o in orders:
            for i in itertools.combinations(o, c):
                temp.append(''.join(sorted(i)))
        mc_temp = Counter(temp).most_common()
        for mc in mc_temp:
            if mc[1] > 1 and mc[1] == mc_temp[0][1]:
                answer.append(mc[0])
    
    return sorted(answer)