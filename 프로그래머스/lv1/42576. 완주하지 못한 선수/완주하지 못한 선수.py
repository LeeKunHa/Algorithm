def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('temp')
    for i,j in zip(participant,completion):
        if i!=j:
            return i