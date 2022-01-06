for i in range(1, 51):
  file = open("{0}주차.txt".format(i), "w", encoding = "utf8")
  file.write("- {0} 주차 주간보고 -".format(i))
  file.write("\n부서 : ")
  file.write("\n이름 : ")
  file.write("\n업무 요약 : ")
file.close()