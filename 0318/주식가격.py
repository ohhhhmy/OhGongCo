def solution(prices):
    from collections import deque
    dq = deque(prices)
    answer = []
    dq_len = len(dq)
    
    for i in range(dq_len):
        price = dq.popleft()
        count = 0
        for j in dq:
            count += 1
            if j < price:
                break
        answer.append(count)
                      
    return answer

print(solution([1,2,3,2,3]))
print(solution([1,2,3,2,3,1]))

# 시간 초과난 코드
# def solution(prices):
#     answer = []
    
#     for i in range(len(prices)):
#         price = prices[i]
#         count = 0
#         others = prices[i + 1:]
#         for j in others:
#             count += 1
#             if j < price:
#                 break
#         answer.append(count)
                      
#     return answer