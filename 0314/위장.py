def solution(c):
    from functools import reduce
    dic = {}

    for wear in c:
        stuff = wear[1]
        if stuff not in dic:
            dic[stuff] = 1
        else:
            dic[stuff] += 1

    count = [i + 1 for i in dic.values()]
    
    answer = reduce(lambda x, y : x * y, count)

    return answer - 1
    
# 예전 풀이
# def solution(c):
#     from itertools import combinations
#     from functools import reduce
#     dic = {}

#     for wear in c:
#         stuff = wear[1]
#         if stuff not in dic:
#             dic[stuff] = 1
#         else:
#             dic[stuff] += 1

#     count = [i for i in dic.values()]
#     key_num = len(count)
    
#     answer = 0
#     for i in range(1, key_num + 1):
#         combi = combinations(count, i)
#         for j in combi:
#             answer +=reduce(lambda x, y : x * y, j)
#     return answer
# 예전 풀이의 문제 : 조합으로 구하다보니 시간 초과가 났다.

#test case
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["glasses", "eyewear"], ["green_turban", "headgear"], ["black_cap", "headgear"], ["short", "pants"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))