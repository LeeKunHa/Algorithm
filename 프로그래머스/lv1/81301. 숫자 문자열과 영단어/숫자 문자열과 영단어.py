def solution(s):
    answer = ''
    num_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8','nine':'9'}
    while len(s)!=0:
        for i in range(1, len(s)+1):
            temp = s[:i]
            if temp in num_dict.keys():
                answer = answer+num_dict[temp]
                s = s[i:]
                break
            elif temp in num_dict.values():
                answer = answer+temp
                s = s[i:]
                break
            else:
                pass
    return int(answer)