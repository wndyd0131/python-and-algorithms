#1
inventory = {'메로나':[300, 20], '비비빅':[400, 3], '죠스바':[250, 100]}
#2
print(inventory['메로나'][0], "원")
#3
print(inventory['메로나'][1], '개')
#4
inventory['월드콘'] = [500, 7]
print(inventory)
#5
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
key_ice = list(icecream.keys())
print(key_ice)
#6
value_ice = list(icecream.values())
print(value_ice)
#7
sum_ice = sum(value_ice)
print(sum_ice)
#8
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
#9
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)
#10
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)
#11
