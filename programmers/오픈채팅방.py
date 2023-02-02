def solution(record):
    uidDict = dict()
    answer = []
    for i in record:
        cmd = i.split()[0]
        if cmd == 'Enter' or cmd == 'Change':
            uid, nick = i.split()[1], i.split()[2]
            uidDict[uid] = nick
    for i in record:
        cmd = i.split()[0]
        if cmd == 'Enter':
            uid = i.split()[1]
            answer.append(uidDict[uid]+"님이 들어왔습니다.")
        elif cmd == 'Leave':
            uid = i.split()[1]
            answer.append(uidDict[uid]+"님이 나갔습니다.")
        else:
            continue
    
    return answer