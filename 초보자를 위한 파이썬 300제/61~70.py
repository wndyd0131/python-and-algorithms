#61
''
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
''
#62
''
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::2])
''
#63
''
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])
''
#64
nums = [1,2,3,4,5]
print(nums[::-1])
#65
''
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])
''
#67 (join 메서드) list -> string
''
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
interest1 = " ".join(interest)
print(interest1)
''
#68
''
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
interest1 = "\n".join(interest)
print(interest1)
''
#69 (split 메서드) string -> list
''
string = "삼성전자/LG전자/Naver"
string1 = string.split("/")
print(string1)
''
#70
data = [2,4,3,1,5,10,9]
data1 = sorted(data)
print(data1)
