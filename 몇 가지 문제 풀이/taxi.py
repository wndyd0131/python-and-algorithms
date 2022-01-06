# -*- coding: utf-8 -*-
import random
count = 0
for i in range(1, 51):
  cust = random.randrange(5, 51)
  if(cust >= 5 and cust <= 15):
    print('[O] {0}번째 손님 (소요시간 : {1}분)'.format(i, cust))
    count += 1
  else:
    print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(i, cust))
print('총 탑승 승객 : {0} 분'.format(count)) 