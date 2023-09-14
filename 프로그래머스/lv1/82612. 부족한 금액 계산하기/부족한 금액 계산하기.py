def solution(price, money, count):
    payment = 0
    price_now = price
    for i in range(1,count+1):
        payment = payment + price_now
        price_now = price_now + price
    answer = payment - money
    if answer < 0:
        answer = 0
    return answer