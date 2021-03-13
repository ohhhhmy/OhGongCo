def solution(s):
    answer = [0, 0]
    # 횟수, 0의 개수

    while s != "1":
        num = 0
        for i in s:
            if i == "1":
                num += 1
            else:
                answer[1] += 1
        s = format(num, 'b')
        answer[0] += 1

    return answer

#test case

print(solution("01110"))