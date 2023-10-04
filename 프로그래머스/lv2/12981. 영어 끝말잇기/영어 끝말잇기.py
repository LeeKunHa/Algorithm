def solution(n, words):
    clear = []
    for i in range(len(words)):
        if clear and clear[-1][-1]!=words[i][0]:
            return [(i%n)+1,(i//n)+1]
        elif words[i] not in clear:
            clear.append(words[i])
        elif (words[i] in clear):
            return [(i%n)+1,(i//n)+1]
    return [0,0]