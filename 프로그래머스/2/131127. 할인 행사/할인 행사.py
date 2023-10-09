def solution(want, number, discount):
    answer = 0
    for day in range(len(discount)-9):
        count = 0
        for x,i in zip(want,number):
            if discount[day:day+10].count(x) >= i:
                count = count+1
            else:
                break
        if count == len(want):
            answer = answer+1
    return answer