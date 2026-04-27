def solution(progresses, speeds):
    '''
    - 기능 개선 작업 (100% 돼야 배포 가능)
    - 기능 개발 속도 다름 -> 뒤에 있는 게 먼저 개발되면 앞에 거 기다려야 함
    - 각 배포마다 한 번에 몇개의 기능이 배포되는지 return
    '''
    answer = []
    days = []
    
    # process data -> days (e.g., [7, 3, 9])
    for progress, speed in zip(progresses, speeds):
        days.append(((100 - progress) + speed - 1) // speed)
        
    count = 1
    current = days[0]
    
    # loop
        # current 보다 작거나 같으면 count += 1
        # 아니면 count 등록 후 current 업데이트
    for i in range(1, len(days)):
        if days[i] <= current:
            count += 1
        else:
            answer.append(count)
            current = days[i]
            count = 1
            
    # 마지막 프로그레스는 따로 처리
    answer.append(count)
        
    return answer

'''
막힌 부분
- Loop 작업에 대한 boundary 설정
  - 변수 초기화 (e.g., count = 1)
    - 첫번째 프로그레스는 무조건 오기 때문에 count = 1로 시작
  - 마지막 progress를 어떻게 처리해야 할지 고민
'''
