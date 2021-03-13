def solution(n):
    nums = bin(n)[2:].count("1")
    count = 0
    num = n + 1
    
    while True:
        bin_num = bin(num)[2:].count("1")

        if bin_num == nums:
            break

        num += 1

    return num

#test case
print(solution(78))
print(solution(15))