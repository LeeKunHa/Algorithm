def solution(n):
    three = ''
    answer = 0
    while n!=0:
        three = three+str(n%3)
        n = n//3
        
    position = 0
    for i in str(three)[::-1]:
        answer = answer + int(i)*3**position
        position = position+1
    return answer