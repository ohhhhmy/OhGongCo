def solution(g, p):

    playlist = {}
    genre_length = len(g)
    list_length = len(p)
    only_number = {}
    play = [] 
    
    for i in range(list_length):
        if p[i] not in only_number:
            only_number[p[i]] = []
        only_number[p[i]].append(i)

    print(only_number)

    for i in range(genre_length):
        if g[i] not in playlist:
            playlist[g[i]] = []
        playlist[g[i]].append(p[i])
        playlist[g[i]].sort(reverse=True)

    #재생 수 합 기준으로 내림차순 정렬
    playlist = sorted(playlist.values(), key = lambda x: sum(x), reverse=True)
    play = [i[:2] for i in playlist]
    
    answer = []
    
    for i in play:
        if len(i) == 1:
            answer.append(only_number[i[0]][0])
        else:
            for j in range(2):
                if len(only_number[i[j]]) == 1:
                    answer.append(only_number[i[j]][0])
                else:
                    answer.append(only_number[i[j]][j])

    return answer

#test case
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic", "pop", "classic", "pop", "classic", "classic"], [400,600,150,600,500,500]))
