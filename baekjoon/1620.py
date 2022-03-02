from distutils.util import change_root
import sys
searcher = dict()
cmd = sys.stdin.readline().split()
p_num = int(cmd[0])
q_num = int(cmd[1])
for i in range(1, p_num + 1):
  pokemon = sys.stdin.readline().strip()
  searcher[pokemon] = i

t = searcher.items()
r_searcher = dict(map(reversed, searcher.items()))

for i in range(q_num):
  q = sys.stdin.readline().strip()
  if q.isnumeric():
    q = int(q)
    print(r_searcher.get(q))
  else:
    print(searcher.get(q))
    
# value 값으로 key 값을 찾기 위해 dict(map(reversed, searcher.items()))를 활용
# searcher.items()는 튜플의 리스트인데, 위 방법은 이를 활용해 튜플을 역으로 정렬한 뒤 딕셔너리로 바꾸는 방식이다