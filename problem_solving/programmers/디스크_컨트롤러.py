# retry
import heapq
from collections import deque
def solution(jobs):
    '''
    대기큐: [{번호, 요청 시각, 소요 시간}]
    번호는 어떻게 저장?
    각각 우선순위에 따라 정렬 어떻게?
    하드디스크 작업x, 대기 큐 not empty = then, 우선순위 높은 작업 대기큐에서 꺼냄
        - 우선순위: 짧은 소요시간 > 빠른 요청 시각 > 작은 번호
    다른 작업 요청 시간이랑 겹치면 -> 작업이 끝나고 나자마자 대기큐에 넣음 -> 우선순위 대로 뽑음
    disk (jobs) -> 요청 시각 -> priority queue -> 우선순위 -> task handler
    priority: ...
        - edge case
            - 작업이 끝날 때 작업이 들어오면, 작업이 끝나고 작업을 대기큐에 넣음
            - 작업이 끝날 때 작업이 들어오지 않으면, 다음 작업 실행
            - 같은 시간에 작업이 여러개 들어오는 경우
    시간에 따라 jobs에서 뺌
    0일 때는 그냥 실행
    이후에는
        priority queue에 들어옴, 들어올 때 heapify
    각각에 대해 처리 시간 저장
    작업 처리 평균 정수
    시간 단위
    '''
    n = len(jobs)
    jobs = deque(sorted(jobs, key=lambda x: x[0])) # 순서대로 오는 보장이 없기 때문에 sort
    cur_idx = 0
    heap = []
    time = 0
    turnaround = 0
    while jobs or heap:
        # 시간에 해당되는거 있으면 대기큐에 삽입
        while jobs and jobs[0][0] <= time: # 이미 지난 job 큐에 넣음
            req, dur = jobs.popleft()
            heapq.heappush(heap, (dur, req, cur_idx))
            cur_idx += 1
        # 현재 실행 중이지 않으면 대기큐에서 드로우 후 시간 계산
        if heap:
            dur, req, idx = heapq.heappop(heap)
            time += dur # 비선점형이니까 한 번에 duration만큼 더함, 선점형이라면 1씩 더할 필요가 있음
            turnaround += time - req
        # 없으면 1씩 올림
        else:
            time += 1
    return turnaround // n
    '''
    key takeaways
        - heap은 튜플을 통해 우선순위 기준을 줄 수 있음
        - 여러 개가 동시에 들어오는 경우 고려
        - 비선점형이라면 시간을 1씩 더하는 것보다 작업 시간 한 번에 더한 다음에 초과한 작업들을 처리하는 방식 고려
        - turnaround = 실제 작업 시간 = 현재 시각 - 요청 시각
    '''