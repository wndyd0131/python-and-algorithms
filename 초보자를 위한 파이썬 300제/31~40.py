#31
'''
#답: 34
'''
#32
'''
#답: HiHiHi
'''
#33
'''
print('-' * 80)
'''
#34
'''
t1 = 'python'
t2 = 'java'
print((t1 + ' ' + t2 + ' ') * 4)
'''
#35 (% formatting)
'''
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
'''
#36 (format 메서드)
'''
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 =  13
print("이름: {0} 나이: {1}".format(name1, age1))
print("이름: {0} 나이: {1}".format(name2, age2))
'''
#37 (f-string)
'''
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 =  13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
'''
#38
'''
상장주식수 = "5,969,782,550"
itg = 상장주식수.replace(',', '')
itg = int(itg)
print(itg, type(itg))
'''
#39
'''
#내 답: 분기 = "2020/03(E) (IFRS연결)"
#내 답: 분기 = 분기.split('(')
#내 답: print(분기[0])
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
'''
#40
'''
data = "   삼성전자   "
print(data.strip())
'''
