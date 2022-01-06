#81
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)
#82
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,_,*valid_score = scores
print(valid_score)
#83
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,*valid_score,_ = scores
print(valid_score)
#84
temp = {}
print(type(temp))
    #아니면
    #temp = dict()
    #print(type(temp))
#85
price = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(price)
#86
price['죠스바'] = 1200
price['월드콘'] = 1500
print(price)
#87
print("메로나 가격: ", price['메로나'])
#88
price['메로나'] = 1300
print(price)
#89
price.pop('메로나')
    #or del price['메로나']
print(price)
#90
    #key값이 딕셔너리에 존재하지 않아서
