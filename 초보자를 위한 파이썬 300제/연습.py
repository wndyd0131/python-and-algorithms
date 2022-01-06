f = open("score.txt", "r", encoding = "utf8")
while True:
  line = f.readline()
  if not line:
    break
  print(line)
f.close()