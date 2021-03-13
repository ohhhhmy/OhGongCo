def solution(citations):
    sortedCitations = sorted(citations)
    citationNum = sortedCitations[len(citations) // 2]
    
    while True:
        testList = [i for i in sortedCitations if i >= citationNum]
        if len(testList) >= citationNum:
            break
        else:
            citationNum -= 1

    return citationNum

#test case
print(solution([3,0,6,1,5]))
            
            