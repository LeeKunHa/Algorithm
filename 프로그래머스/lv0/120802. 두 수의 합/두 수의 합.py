def solution(num1, num2):
    if num1 > 50000 or num1 < -50000:
        answer = "num1 의 값을 다시 입력하세요."
    elif num2 > 50000 or num2 < -50000:
        answer = "num2 의 값을 다시 입력하세요."
    else: 
        answer = num1 + num2
    return answer