def solution(price, money, count):
    payment = 0
    price_ = price
    for i in range(1,count+1):
        payment = payment + price_
        price_ = price_ + price
    answer = payment - money
    if answer < 0:
        answer = 0
    return answer