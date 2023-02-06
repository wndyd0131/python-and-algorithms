# Ascend according:
    # 자주 나오는 단어
    # 길수록
    # 알파벳 순서
# 특정 길이 이상인 거만 외움
import sys
from collections import Counter
word_list = []
result = []
N, L = sys.stdin.readline().split()
N, L = int(N), int(L)
for i in range(N):
    word = sys.stdin.readline().strip()
    if len(word) >= L:
        word_list.append(word)

sorted_word_list = sorted(word_list)
sorted_word_list = sorted(sorted_word_list, key=len, reverse=True)
MC = Counter(sorted_word_list).most_common()
for mc in MC:
    print(mc[0])