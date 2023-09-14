def solution(phone_number):
    answer = '*' * (len(phone_number)-4)
    phone_number =  phone_number[-4:]
    answer = answer+phone_number
    return answer