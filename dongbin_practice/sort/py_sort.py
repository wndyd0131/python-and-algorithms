array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)

print(result)

array = ['좋은하루', '와', '이건좀', '멋진 것 같다']

result = sorted(array, key=len)

print(result)

array = ['heymzn', 'heymcn', 'heyman', 'heymkn']

result = sorted(array, key=lambda x: x[4])

print(result)