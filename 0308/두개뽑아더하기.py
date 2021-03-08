#combinations
from itertools import combinations

def solution(numbers):
    comNumbers = [sum(i) for i in combinations(numbers, 2)]

    return sorted(list(set(comNumbers)))


#이중for문
def solution2(numbers):
    ans = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num = numbers[i] + numbers[j]
            if num not in ans:
                ans.append(num)

    return sorted(ans)


#test cases
print(solution2([2,1,3,4,1]))
print(solution([5,0,2,7]))