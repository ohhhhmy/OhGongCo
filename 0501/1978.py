n = int(input())

nums = [i for i in map(int, input().split())]

cnt = 0 # 소수 개수
for i in nums:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        cnt += 1

print(cnt)
