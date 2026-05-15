# retry
import heapq
def solution(operations):
    '''
    solution
    0. heap 두개 생성
    0-1. dictionary 생성 key = id
    0-2. insert시 id tracking용 cur_id 변수
    1. parse operations
    2. 조건문
        a. I면
            maxheap은 heappush(heap, (-val,id))
            minheap은 heappush(heap, (val, id))
            cur_id += 1
        b. D이고 1이면
            maxheap은 heappop
            minheap은 id찾아서 삭제 후 heapify
            비어있으면 무시
        c. D이고 -1이면
            minheap은 heappop
            maxheap은 id찾아서 삭제 후 heapify
            비어있으면 무시
    3. 결과 반환
    - 비어 있으면 [0,0]
    - 아니면 [최댓값, 최솟값]
    
    힙 두 개 생성 후 함께 삭제
        - 최솟값 삭제
            - 최대힙에서 바이너리 서치를 통해 값 삭제 후 heapify
        - 최댓값 삭제
            - 최소힙에서 "
        - 힙을 두개 생성
            - High space complexity
    공유힙
        - 정렬할 때마다 최소힙 최대힙으로 바꿔야 함
    
    edge case
    questions
    - 힙에서 특정 엘리먼트 삭제 가능?
        - 배열이면 pop하고 heapify 해주면 됨
    - 최소힙에서 최대힙으로 전환 가능?
        - 최대힙으로 변경 하려면 최댓값을 탐색해야 하기 때문에 O(n)으로 비효율적임
    '''
    max_heap, min_heap = [], []
    cur_id = 1
    for operation in operations:
        cmd, val = operation.split()
        if cmd == 'I':
            heapq.heappush(max_heap, (-int(val), cur_id))
            heapq.heappush(min_heap, (int(val), cur_id))
            cur_id += 1
        elif cmd == 'D' and val == '1' and max_heap and min_heap:
            data, id = heapq.heappop(max_heap)
            for i in range(len(min_heap)):
                if min_heap[i][1] == id:
                    min_heap.pop(i)
                    heapq.heapify(min_heap)
                    break
        elif cmd == 'D' and val == '-1' and max_heap and min_heap:
            data, id = heapq.heappop(min_heap)
            for i in range(len(max_heap)):
                if max_heap[i][1] == id:
                    max_heap.pop(i)
                    heapq.heapify(max_heap)
                    break
    if max_heap and min_heap:
        return [-max_heap[0][0], min_heap[0][0]]
    else:
        return [0,0]
    answer = []
    return answer

import heapq
def solution(operations): # 문제 있는 코드
    '''
    반대편 삭제 타이밍
    while min_heap and deleted.get(min_heap[0][1]):
      heapq.heappop(min_heap)
    해당 코드가 max_heap의 heappop 보다 늦게 실행되면, max_heap에 삭제 데이터가 남아서 데이터 일관성이 깨질 가능성이 있음
    '''
    max_heap, min_heap = [], []
    deleted = {}
    cur_id = 1
    for operation in operations:
        cmd, val = operation.split()
        if cmd == 'I':
            heapq.heappush(max_heap, (-int(val), cur_id))
            heapq.heappush(min_heap, (int(val), cur_id))
            cur_id += 1
        elif cmd == 'D' and val == '1' and max_heap and min_heap:
            data, id = heapq.heappop(max_heap)
            while min_heap and deleted.get(min_heap[0][1]):
                heapq.heappop(min_heap)
            deleted[id] = True
        elif cmd == 'D' and val == '-1' and max_heap and min_heap:
            data, id = heapq.heappop(min_heap)
            while max_heap and deleted.get(max_heap[0][1]):
                heapq.heappop(max_heap)
            deleted[id] = True
    while min_heap and deleted.get(min_heap[0][1]):
        heapq.heappop(min_heap)
    while max_heap and deleted.get(max_heap[0][1]):
        heapq.heappop(max_heap)
    if max_heap and min_heap:
        return [-max_heap[0][0], min_heap[0][0]]
    else:
        return [0,0]
    
import heapq
def solution(operations): # 위 문제 해결 코드
    '''
    여기서는 각각 처리 중인 힙에 대해 heappop하기 전에 반대편 힙의 쓰레기 데이터를 미리 다 삭제해서 일관성이 꺠질 일 없음
    '''
    max_heap, min_heap = [], []
    deleted = {}
    cur_id = 1
    for operation in operations:
        cmd, val = operation.split()
        if cmd == 'I':
            heapq.heappush(max_heap, (-int(val), cur_id))
            heapq.heappush(min_heap, (int(val), cur_id))
            cur_id += 1
        elif cmd == 'D' and val == '1' and max_heap and min_heap:
            while min_heap and deleted.get(min_heap[0][1]):
                heapq.heappop(min_heap)
            data, id = heapq.heappop(max_heap)
            deleted[id] = True
        elif cmd == 'D' and val == '-1' and max_heap and min_heap:
            while max_heap and deleted.get(max_heap[0][1]):
                heapq.heappop(max_heap)
            data, id = heapq.heappop(min_heap)
            deleted[id] = True
    while min_heap and deleted.get(min_heap[0][1]):
        heapq.heappop(min_heap)
    while max_heap and deleted.get(max_heap[0][1]):
        heapq.heappop(max_heap)
    if max_heap and min_heap:
        return [-max_heap[0][0], min_heap[0][0]]
    else:
        return [0,0]

'''
key takeaways
1. 반대힙 바로 삭제 vs. lazy deletion
    - 삭제할 때마다 반대힙에 대해서 id를 탐색해야 하기 때문에 비효율적임
        - 배열이나 딕셔너리를 통해서 삭제된 id를 저장만 해둔 뒤에 heappop을 할 타이밍에 top이 이미 삭제된 id면 버림
2. 반대힙 삭제 타이밍에 의한 데이터 일관성 고려
'''