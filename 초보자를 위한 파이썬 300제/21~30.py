#21
'''
letters = "python"
print(letters[0],letters[2])
'''
#22
'''
license_plate = "24가 2210"
print(license_plate[4:])
'''
#23
'''
string = "홀짝홀짝홀짝"
print(string[::2])
'''
#24
'''
string = "PYTHON"
print(string[::-1])
'''
#25
'''
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))
'''
#26
'''
phone_number = "010-1111-2222"
print(phone_number.replace('-', ''))
'''
#27
'''
#내 답: url = "http://sharebook.kr"
#내 답: print(url[url.index('.') + 1:])

#좋은 답:
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])
'''
#28
'''
#답: 문자열 인덱스 안의 값은 변경시킬 수 없음
'''
#29
'''
string = 'abcdfe2a354a32a'
string1 = string.replace('a','A')
print(string1)
'''
#30
''
#답: abcd / 이유는 문자열 자체는 변경될 수 없어서, replace함수는 새로운 객체를 돌려주기 때문에 원본이 변경되지는 않는다.
''
