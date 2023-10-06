from collections import Counter
def solution(k, tangerine):
    tangerine = Counter(tangerine).most_common()
    answer = []
    for i in tangerine:
        for j in range(i[1]):
            answer.append(i[0])
    answer = len(set(answer[:k]))
    return answer