'''
def is_odd(item):
    if item % 2 == 0:
        return "짝수"
    else:
        return "홀수"

data = int(input("값을 입력하세요: "))
print(is_odd(data))
'''
'''
def avg(*args):
    s = 0
    for arg in args:
        s += arg
    return s/len(args)


print(avg(70,80,60))
        
'''
'''
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
'''
'''
(3)
print("you","need","python")
'''
'''
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
'''
'''
input1= input("입력: ")
f = open("test.txt", 'a')
f.write(input1)
f.write("\n")
f.close()
'''
f = open("test.txt", 'r')
data = f.read()
f.close()

data = data.replace("java", "python")

f = open("test.txt", 'w')
f.write(data)
f.close()
