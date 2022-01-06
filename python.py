"""
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % (coffee))
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
"""
"""
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번째 학생 축하합니다. 합격입니다." % number)
    else:
        continue
"""
"""
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')
"""
result = [x * y for x in range(2, 10)
                for y in range(1, 10)]
print(result)
