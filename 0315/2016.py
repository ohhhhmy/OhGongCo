def solution(a, b):
    date = 0
    thirtyone = [1,3,5,7,8,10,12]
    days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    if(a == 1):
        date += b
    elif(a == 2):
        date += 31
    elif(a > 2):
        for i in range(1, a):
            if i in thirtyone:
                date += 31
            elif i == 2:
                date += 29
            else:
                date += 30

    if(a != 1):
        date += b

    return days[date % 7]


# 1월 1일은 금요일
# 7로 나눈 나머지가 1이면 금요일
# 조금 더 간단한 방법이 있을 듯 --;;

#test case
print(solution(1, 1))
print(solution(2, 28))
print(solution(2, 29))
print(solution(5, 24))

