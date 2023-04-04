def solution(babbling):
    pronoun = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling:
        while True:
            if i[:3] == 'aya' or i[:3] == 'woo':
                i = i[3:]
            elif i[:2] == 'ye' or i[:2] == 'ma':
                i = i[2:]
            elif len(i) == 0:
                answer = answer+1
                break
            else:
                break
    return answer