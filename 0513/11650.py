num = int(input())
points = []
for i in range(num):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda x : (x[0], x[1]))

for x, y in points:
    print(x,y)
    
# 2단계 정렬 => lambda 식을 이용한다 튜플로 만들어 정렬