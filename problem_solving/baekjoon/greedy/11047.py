import sys
N, A = sys.stdin.readline().split()
N, A = int(N), int(A)
count = 0
money = []
for _ in range(N):
    inpt = int(sys.stdin.readline())
    money.append(inpt)
money.reverse()
for i in money:
    count += A // i
    A = A % i

print(count)