def solution(prices):
    '''
    # 초 단위
    # 주식 가격
    # [1,2,3,2,3]
    # [4,3,1,]
    # 브루트포스 i, j 루프
        # j가 i보다 작을 때까지 셈
    # 1,2,2,3
    # [0,0,1,0,0]
    # 스택
        # 스택 []
    '''
    answer = [0] * len(prices)
    stack = []
    
    # prices에 대해 i부터 n-1까지 (마지막 생략)
    for i in range(len(prices) - 1):
        # while stack and top > prices[i]
            # then pop top and record until stack is empty or top <= prices[i]
        while stack and prices[stack[-1]] > prices[i]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i) # push index
    while stack: # 끝났을 때 남은 주식 계산
        prev = stack.pop()
        answer[prev] = len(prices) - 1 - prev # 각각 마지막 인덱스로부터의 차이 계산
        
    return answer

# 패턴
    # 점차적으로 올라가다가 조건에 따라 sequential하게 감소하는 패턴 = 스택

# Key takeaway
    # 시간을 인덱스 차이로 계산
    # 인덱스를 스택에 저장