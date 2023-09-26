from collections import Counter
def solution(strArr):
    count_list = [len(x) for x in strArr]
    answer = Counter(count_list).most_common(1)[0][1]
    return answer