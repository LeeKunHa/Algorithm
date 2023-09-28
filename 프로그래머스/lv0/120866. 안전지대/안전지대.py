def solution(board): #배열의 크기를 확장시키는 것도 좋아보임
    answer = 0
    n = len(board)-1
    boom = []
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y]==1:
                boom.append([x,y])
                
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,1,0,-1]
    for i in boom:
        for j in range(len(dx)):
            x = i[0]+dx[j]
            y = i[1]+dy[j]
            if 0<=x<=n and 0<=y<=n:
                board[x][y]=1
    answer = sum([x.count(0) for x in board])
    return answer