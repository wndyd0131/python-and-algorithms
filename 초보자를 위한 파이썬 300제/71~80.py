#71
''
my_variable = ()
print(type(my_variable))
''
#72
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)
#73
num = (1,)
print(num)
#74
    #튜플은 원소를 변경할 수 없다
#75
    #튜플
#76
t = ('a','b','c')
t = ('A', 'b', 'c')
    #튜플은 원소를 바꿀 수 없어서 재정의 해야됨
#77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)
#78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(interest)
#79 (#언패킹)
temp = ('apple', 'banana', 'cake')
a,b,c = temp
print(a,b,c)
#80
num = tuple(range(2,100,2))
print(num)
