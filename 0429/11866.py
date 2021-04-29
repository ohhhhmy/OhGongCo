from collections import deque
N, K = map(int, input().split())

nums = [i for i in range(1, N+1)]
dq = deque(nums)

print("<", end="")
while len(dq) > 1:
    for i in range(K):
        if i == K - 1:
            print(dq.popleft(), end=", ")
        else:
            dq.append(dq.popleft())

print(dq.popleft(), ">", sep="")

# count 변수로 하나씩 증가시키면서 count가 3이 아닐 때 popleft()한 수 다시 append하는 것 보단
# 그냥 for문 돌리면서 체크하는게 훨씬 나은 듯

