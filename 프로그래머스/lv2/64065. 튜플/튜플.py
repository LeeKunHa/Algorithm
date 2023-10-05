from collections import Counter
def solution(s):
    s = s.replace('{','').replace('}','').replace(',',' ').split()
    counter = Counter(s)
    answer = list(map(int,[x[0] for x in counter.most_common()]))
    return answer