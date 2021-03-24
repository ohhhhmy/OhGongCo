def solution(n, m):
    a, b = n, m

    if(a > b):
        a,b = b, a

    # 유클리드 호제법
    while b != 0:
        greatest = b
        a, b = b, a % b

    return [greatest, (n * m) // greatest]


#test case
print(solution(4, 7))
print(solution(3, 12))

# 최소공배수는 두 숫자의 곱 나누기 최대공약수다...
