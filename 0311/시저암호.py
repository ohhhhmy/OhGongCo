def solution(s, n):
    # ord => return 숫자
    # chr => return 문자

    answer = ""
    for i in s:
        num = ord(i)
        char = chr(num + n)
                
        if num == 32:
            answer += " "
        elif char.isalpha() and i.isupper() == char.isupper():
            answer += char
        else:
            answer += chr(num + n - 26)

    return answer

#test case
print(solution("AB", 1))
print(solution("z", 1))
print(solution("Z", 10))
print(solution("a B z", 4))
print(solution(" aBZ", 20))
print(solution("y X Z", 4))
print(solution("  h z", 20))

