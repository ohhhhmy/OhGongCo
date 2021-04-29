#1181

import sys
import operator

sys.stdin = open("a.txt", "rt")

num = int(input())
words = []
for i in range(num):
    words.append(input())

wordsSet = list(set(words))

newWords = []
for i in wordsSet:
    ordNum = 0
    for w in i:
        ordNum += ord(w)
    newWords.append({"len" : len(i), "word": i})

newWords.sort(key=operator.itemgetter("len", "word"))

for i in newWords:
    print(i["word"])

# 사전 순 정렬 -> 그냥 단어 기준으로 정렬해주면 되는 것
# itemgetter -> 정렬 기준이 여러 개일 때 매우 유용함
