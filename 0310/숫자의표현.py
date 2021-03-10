def solution(n):
    count = 1
    
    for i in range(1, n // 2 + 1):
        num = i
        sum = 0
        while True:
            sum += num
            num += 1
            
            if sum == n:
                count += 1
                break
                
            if sum > n:
                break
    return count