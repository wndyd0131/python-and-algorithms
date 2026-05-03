def solution(bridge_length, weight, truck_weights): # Fail
  '''
      # truck weights
      # bridge_length
      # weight
      # 2 10 [7,4,5,6]
          # [7,] [4,5,6]
          # 1
      # 7, 4가 함께 오면 안 됨
      # 7만 올 수 있음
      # = 합이 무게를 넘겨서
      # 더이상 더할 수 없으면 count += 1
          # 합이 무게를 넘음
          # array꽉 참
      # Loop end
      # Truck weight가 빌 때까지 진행
          # bridge_length 길이만큼 반복
              # count += 1
              # weights가 비어 있지 않고 queue의 합과 다음인덱스의 합이 weight를 넘기지 않나?
                  # 그럼 pop and append
                  # 아니면 continue
          # 비우기
          # [] 
  '''
  elapsed = 0
  bridge = []
  while truck_weights:
      for i in range(bridge_length):
          elapsed += 1
          if len(bridge) == bridge_length:
              break
          if truck_weights and sum(bridge) + truck_weights[0] <= weight:
              bridge.append(truck_weights.pop(0))
      bridge.pop(0)
  return elapsed

from collections import deque
def solution(bridge_length, weight, truck_weights): # Pass
    elapsed = 0
    cur_weight = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    while trucks:
        elapsed += 1
        
        cur_weight -= bridge.popleft() # 다리에서 하나 내려옴
        
        if cur_weight + trucks[0] <= weight:
            cur_weight += trucks[0]
            bridge.append(trucks.popleft())
        else: # 올릴 수 없으면 0 올림
            bridge.append(0)
    elapsed += bridge_length # 마지막 트럭 내보내기
    return elapsed

'''
Key takeaway
# queue + 시간 단위 시뮬레이션 문제
  # 상태를 '값'이 아닌 '시간 흐름 속 위치'로 모델링
    # solution1은 다리에서 언제 나가는지 표현하지 못함 (e.g., [7,4,5] vs. [7,0,0,4,5]) 
    # solution2는 루프마다 시간을 진행하되 bridge의 빈공간을 [0,0,...]로 상태로 표현함으로써 시간 계산함
'''

