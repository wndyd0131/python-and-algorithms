import sys
equation = sys.stdin.readline().strip()
temp = ''
sum = 0
lst = []
for i in range(len(equation)):
    if equation[i].isdigit():
        temp += equation[i]
        if i == len(equation)-1:
            sum += int(temp)
            lst.append(sum)
            temp = ''
    else:
        if equation[i] == '-':
            sum += int(temp)
            lst.append(sum)
            temp = ''
            sum = 0
        else:
            sum += int(temp)
            temp = ''

num = lst[0]
for i in range(1, len(lst)):
    num -= lst[i]
print(num)