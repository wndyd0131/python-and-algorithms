'''
a = "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
'''
'''
i = 1
s = 0
while i <= 1000:
    if i % 3 == 0:
        s += i
    i += 1
print(s)

'''
'''
i = 1
while i <= 5:
    print('*' * i)
    i += 1
'''
'''
for i in range(1, 101):
    print(i)
'''
'''
s = 0
a = [70,60,55,75,95,90,80,80,85,100]
for i in a:
    s += i
print(s / len(a))
'''
'''
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result)
'''
#-> 리스트 내포
'''
numbers = [1,2,3,4,5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)
'''

