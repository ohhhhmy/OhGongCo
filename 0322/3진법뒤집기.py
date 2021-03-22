def solution(n):
    from collections import deque
    num = n
    remain = 0
    dq = deque()

    while num != 0:
        remain = num % 3
        dq.append(remain)
        
        num = num // 3
    
    while dq[0] == 0:
        dq.popleft()

    answer = 0
    length = len(dq)
    j = 0
    for i in range(length - 1, -1, -1):
        answer += dq[i] * (3 ** j)
        j += 1
    
    return answer
    


print(solution(45))