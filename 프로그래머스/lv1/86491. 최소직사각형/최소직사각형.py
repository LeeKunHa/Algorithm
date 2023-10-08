def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            sizes[i][0],sizes[i][1] = sizes[i][1],sizes[i][0]
    answer = max([x[0] for x in sizes])*max([x[1] for x in sizes])
    return answer