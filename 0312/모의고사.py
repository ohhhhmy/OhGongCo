def solution(answers):
    answer_len = len(answers)

    one = [1,2,3,4,5] * (answer_len // 5 + 1)
    two = [2,1,2,3,2,4,2,5] * (answer_len // 8 + 1)
    three = [3,3,1,1,2,2,4,4,5,5] * (answer_len // 10 + 1)
    answer_len = len(answers)
    i = 0
    j = 0
    k = 0
    count = [0, 0, 0]

    for o in one:
        if answers[i] == o:
            count[0] += 1
        i += 1

        if i == answer_len:
            break

    for t in two:
        if answers[j] == t:
            count[1] += 1
        j += 1

        if j == answer_len:
            break

    for th in three:
        if answers[k] == th:
            count[2] += 1
        k += 1
        
        if k == answer_len:
            break

    print("count :", count)
        
    ans = []
    mx = max(count) 
    for i in range(len(count)):
        if count[i] >= mx:
            ans.append(i + 1)
            mx = count[i]

    return ans

#test case
print(solution([1,2,3,4,5]))
print(solution([2,3,4]))