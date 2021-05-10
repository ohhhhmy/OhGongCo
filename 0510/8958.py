n = int(input())

for i in range(n):
    score = 0
    ox = input().split("X")
    for i in ox:
        for j in range(len(i)):
            score += j + 1
    print(score)

# ox 점수 구하기 문제.
# o들의 index + 1을 점수에 더해주면 된다.