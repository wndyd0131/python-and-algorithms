# 내 것
# site = input()
# site = site[7:]
# site = site.split('.')
# password = site[0][0:3] + str(len(site[0])) + str(site[0].count('e')) + '!'
# print(password)

#or
#강의 것
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print('{0}의 비밀번호는 {1} 입니다.'.format(url, password))