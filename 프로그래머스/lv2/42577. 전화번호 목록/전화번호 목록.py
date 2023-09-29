def solution(phone_book):
    phone_book = sorted(phone_book)
    for i,j in zip(phone_book,phone_book[1:]):
        if i == j[:len(i)]:
            return False
    return True