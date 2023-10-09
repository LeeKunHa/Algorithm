def solution(str1, str2):
    str1 = [str1[i:i+2] for i,x in enumerate(str1[:-1])]
    str1 = [x.lower() for x in str1 if x.isalpha()]
    str2 = [str2[i:i+2] for i,x in enumerate(str2[:-1])]
    str2 = [x.lower() for x in str2 if x.isalpha()]
    both = []
    if len(str1)+len(str2) == 0:
        answer = 65536
    else:
        for i in str1:
            if i in str2:
                both.append(i)
                str2.remove(i)
        answer = len(both)/(len(str1)+len(str2))
        answer = int(answer*65536)
    return answer