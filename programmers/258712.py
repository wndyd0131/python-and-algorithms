# 가장 많이 받은 선물 (2024 KAKAO WINTER INTERNSHIP)
def solution(friends, gifts):
    '''
    DSA used
      - 2D array, hash map, row sum, col sum
    '''

    # name_to_index
    name_index = {}
    for idx, friend in enumerate(friends):
        name_index.setdefault(friend, idx)

    # create 2D array for gift record and initialize
    n = len(name_index)
    gift_record = [[0]*n for _ in range(n)]
    
    for gift in gifts:
        sender, receiver = gift.split()
        sender_idx, receiver_idx = name_index[sender], name_index[receiver]
        gift_record[sender_idx][receiver_idx] += 1
    
    # row_sum
    given = [sum(row) for row in gift_record]
    # col_sum
    received = [sum(col) for col in zip(*gift_record)]
    
    gift_points = [given[i] - received[i] for i in range(n)]
    
    next_receives = [0] * n
    
    # based on gift record, calculate the logic
    for i in range(n):
        for j in range(i + 1, n):
            if gift_record[i][j] > gift_record[j][i]:
                next_receives[i] += 1
            elif gift_record[i][j] < gift_record[j][i]:
                next_receives[j] += 1
            else: # 선물지수 사용
                if gift_points[i] > gift_points[j]:
                    next_receives[i] += 1
                elif gift_points[i] < gift_points[j]:
                    next_receives[j] += 1
    return max(next_receives)
        
    
# 지수 = 준 수 - 받은 수
# if 기록
# if 이번달 A > B
    # then 다음 달 A += 1
# if no 기록 or 주고받은 수 같음
    # if A의 지수 > B의 지수:
        # then A += 1
    # else
        # continue
        
# the greatest value among elements