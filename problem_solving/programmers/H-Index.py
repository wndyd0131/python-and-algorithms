# retry
def solution(citations):
    '''
    [3,0,6,1,5] 5편
    [0,1,3,5,6] 0번 이상 0 편 이상, 1번 이상 1편 이상, 3번 이상 3편이상, 5번 이상 5편이상x
    [0,1,5,50,100,1000,1001,1002] 이러면 5
    [8] 이러면 0
    
    [6,5,3,1,0]
    '''
    cur_max = 0
    citations = sorted(citations, reverse=True)
    for i, c in enumerate(citations):
        cur = 0
        if c >= i + 1:
            cur_max += 1
        else:
            break
    return cur_max
'''
key takeaways:
1. 정렬함으로써 O(n^2)을 O(n)으로 만듦. 즉, 이전 값에 대한 재계산할 필요가 없어짐 
'''