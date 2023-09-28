def solution(numlist, n):
    answer = [x[1] for x in sorted([[abs(x-n)+n,numlist[i]] for i,x in enumerate(numlist)], key=lambda x:(x[0],-x[1]))]
    return answer