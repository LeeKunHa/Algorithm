def solution(id_pw, db):
    answer = 'fail'
    for i in range(len(db)):
        if db[i][0]==id_pw[0]:
            answer = 'wrong pw'
            if db[i][1]==id_pw[1]:
                answer = 'login'
    return answer