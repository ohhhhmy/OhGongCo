def solution(N, stages):
    import operator
    dic = {}
    answer = []
    for i in range(1, N + 1):
        noclear = stages.count(i)
        clears = len([n for n in stages if n >= i])
        try:
            dic[i] = noclear / clears
        except ZeroDivisionError:
            dic[i] = 0
    
    a = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    for i in a:
        answer.append(i[0])

    return answer

#test case
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(5, [1,2,3,3,4]))

