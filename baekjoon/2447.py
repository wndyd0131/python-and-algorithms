def square(N):
  if N == 3:
    print('***')
    print('* *')
    print('***')
    return
  square(N//3)
square(3)