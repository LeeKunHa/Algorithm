def solution(s):
    answer = []
    if len(s)==1:
        return 1
    for i in range(1,(len(s)//2)+1):
        temp = ''
        count = 1
        cyc = s[:i]
        for j in range(i,len(s)+i,i):
            if cyc == s[j:j+i]:
                count = count+1
            else:
                if count>1:
                    temp = temp+str(count)+cyc
                else:
                    temp = temp+cyc
                count = 1
                cyc = s[j:j+i]
        answer.append(len(temp))
    return min(answer)