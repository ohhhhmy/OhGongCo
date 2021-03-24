# def solution(b, y):
#     if(b == 8 and y == 1):
#         return [3, 3]

#     answer = []

#     for i in range(1, y // 2 + 1):
#         width = y // i # 노란색 가로 개수
#         height = i

#         for j in range(2, 10, 2):
#             if(width * 2 + height * j + 4 == b):
#                 answer.append(width + 2)
#                 answer.append(height + j)
#                 return answer

def solution(b, y):
    tiles = b + y
    
    for i in range(1, tiles // 2 + 1):
        if tiles % i == 0:
            width = tiles // i
            height = i

            if (width - 2) * (height - 2) == y:
                return [width, height]
        


#test case
print(solution(24, 24))
print(solution(8, 1))
print(solution(18, 6))
print(solution(40, 8)) # 12 5