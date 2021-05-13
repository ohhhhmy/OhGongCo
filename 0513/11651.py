num = int(input())
points = []
for i in range(num):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda x : (x[1], x[0]))

for x, y in points:
    print(x,y)

# y좌표 순 정렬이면 x[1]을 첫 번째 기준으로