def solution(hp):
    n = hp//5
    n = n + hp%5//3
    n = n + hp%5%3//1
    answer = n
    return answer