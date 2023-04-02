def solution(sides):
    if (sides[0] + sides[1] > sides[2]) and (sides[0] + sides[2] > sides[1]) and (sides[1] + sides[2] > sides[0]):
        answer = 1
    else:
        answer = 2
    return answer