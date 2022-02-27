import sys
alpha = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
ch = sys.stdin.readline().strip()
for i in range(len(ch)):
  alp = ch[i].lower()
  alpha[alp] += 1
  
num_list = list(alpha.values())
mx = max(num_list)
if num_list.count(mx) > 1 or num_list.count(mx) == 0:
  print('?')
else:
  print(chr(65 + num_list.index(mx)))