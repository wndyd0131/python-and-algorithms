import pymysql

conn = pymysql.connect(user='root', passwd='@rjy153101', host='localhost', db='testdb',charset='utf8') # 커넥션(연결)
curs = conn.cursor(pymysql.cursors.DictCursor) # 커서
sql = "select * from table1 where col2 = %s" # SQL 명령어
curs.execute(sql, 'wndyd')

rows = curs.fetchall() # 모든 데이터를 가져옴
print(rows)

for row in rows:
  print(row)
  print(row[0])

conn.close()