def solution(people, limit):
    answer = 0
    people = sorted(people,reverse=True)
    start = 0
    end = len(people)-1
    while start <= end:
        if people[start]+people[end] <= limit:
            start = start+1
            end = end-1
        else:
            start = start+1
        answer = answer+1
    return answer