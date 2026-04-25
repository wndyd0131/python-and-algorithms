from collections import deque
def solution(priorities, location):
    count = 0
    priorities = deque([(priorities[i], i) for i in range(len(priorities))])
    while priorities:
        cur_max = max(priorities)[0]
        print(cur_max)
        if priorities[0][0] != cur_max:
            priorities.append(priorities.popleft())
        else:
            priority = priorities.popleft()
            count += 1
            if priority[1] == location:
                break
    return count
  
'''
Thought process
'''
    # [2,1,3,2], 2, 1
    # [1,3,2,2]
    # [3,2,2,1]
    # step
        # create new tuple array applying identifier
        # iterate while array is not empty
            # condition based on max value
            # if identifier is removed, break
    
    # priorities
        # priority tracking how?
            # get max for each iteration
            # 
    # location
        # apply identifier to each process
    # return the order in which it is executed