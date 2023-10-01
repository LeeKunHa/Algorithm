def solution(a, b):
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [0,31,29,31,30,31,30,31,31,30,31,30]
    answer = days[(sum(months[:a])+b)%7-1]
    return answer