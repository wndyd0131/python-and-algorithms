import heapq

def solution(scoville, K):
    '''
    문제 정의
    스코빌 지수 가장 낮은 두 개
    최소 횟수
    
    그리디, 우선순위, 큐
    
    예시
    [1, 2, 3, 9, 10, 12], 7
    1 + 2*2 = 5
    [5,3,9,10,12]
    3 + 5*2 = 13
    [13,9,10,12]
    정답: 2
    
    [4,1,3,2], 4
    1 + 2*2 = 5
    [5,4,3]
    
    접근
    1. 브루트포스 sort = 비효율적
    2. 가장 매운거, 두번째로 매운거 실시간으로 알아야 함 = 힙 sort
    
    1. scoville을 min heap으로 만듦
    2. heap이 두 개 이상인가? and top이 K보다 작은가?
        2-1. if then, 가장 매운거랑 두번째 매운거 pop한 뒤 조합하여 넣고 heappush
            - count 올림
        2-2. else, break
    
    edge case
    1. K이상으로 만들 수 없는 경우
        ex) [1, 2], 4
        1-1. 전부 합쳤는데 마지막 조합이 K보다 작음
    2. 처음부터 모든 음식이 K이상인 경우
        return 0
    '''
    count = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        count += 1
    if scoville[0] < K:
        return -1
    return count
  
  
def solution(scoville, K):
    '''
    더 깔끔한 버전
    
    while scoville[0] < K:
      if len(scoville) < 2:
        return -1
    '''
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        count += 1
    return count     
    
# Key takeaway
'''
1. 특정한 우선순위대로 뽑는 경우 힙 고려
2. 최소 횟수 = 최소힙 사용 시 보장
'''