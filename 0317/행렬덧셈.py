def solution(arr1, arr2):
    answer = []
    length = len(arr1);
    
    for i in range(length):
        arr = [sum(i) for i in list(zip(arr1[i], arr2[i]))]
        answer.append(arr)
        
    return answer
    
#test case
print(solution([[1,2],[2,3]], [[3,4],[5,6]]))