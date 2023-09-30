def solution(date1, date2):
    date1 = ''.join(map(str,(date1)))
    date2 = ''.join(map(str,(date2)))
    if int(date1) < int(date2):
        return 1
    else:
        return 0