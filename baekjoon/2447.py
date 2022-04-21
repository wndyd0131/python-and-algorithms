def square(N):
  if N == 3:
    for i in range(N): print('*')
    print('* *')
    print('***')
    return
  square(N//3)
square(3)