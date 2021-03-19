def solution(new_id):
    import re
    # 1단계
    lower = new_id.lower()

    # 2단계
    word = re.sub("[^0-9a-z_.-]","", lower)
  
    # 3단계
    word = re.sub(r"[\b.]+", ".", word)

    # 4단계 
    word = word.strip(".")

    # 5단계   
    if len(word) == 0:
        word = "a"
    # 6단계
    elif len(word) >= 16:
        word = word[:15].strip(".")

    # 7단계
    if len(word) <= 2:
        while len(word) != 3:
            word += word[-1]

    return word

#test case
print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("123_.def"))
