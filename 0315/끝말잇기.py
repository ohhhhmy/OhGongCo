def solution(n, words):
    answer = []
    answers = [words[0]]
    words_length = len(words)
    
    for i in range(1, words_length):

        if words[i -1][-1:] != words[i][:1] or words[i] in answers:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break

        answers.append(words[i])    
    

    if len(answer) == 0:
        return [0, 0]
    else:
        return answer

# test case
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,  	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
print(solution({"abb", "baa", "ccc", "cda", "abb"}))