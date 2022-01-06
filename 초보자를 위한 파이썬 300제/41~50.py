#41
'''
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)
'''
#42
'''
ticker = "BTC_KRW"
ticker1 = ticker.lower()
print(ticker1)
'''
#43
'''
ticker = "hello"
ticker1 = ticker.capitalize()
print(ticker1)
'''
#44
'''
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
'''
#45'
'''
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx", "xls")))
'''
#46
'''
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))
'''
#47
'''
a = "hello world"
print(a.split())
'''
#48
'''
ticker = "btc_krw"
ticker = ticker.split("_")
print(ticker)
'''
#49
'''
date = "2020-05-01"
date = date.split('-')
print(f"연도: {date[0]} 월: {date[1]} 일: {date[2]}")
'''
#50
'''
data = "039490      "
print(data.rstrip())
'''
