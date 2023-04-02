def solution(lines):
    answer = 0
    a,b,c = [],[],[]
    all_ = []
    for line in lines:
        temp = []
        for i in range(line[0],line[1]):
            temp.append(i)
        all_.append(temp)
    answer = len(set(all_[0]).intersection(set(all_[1])))+len(set(all_[0]).intersection(set(all_[2])))+len(set(all_[1]).intersection(set(all_[2])))-(len(set(all_[0]).intersection(set(all_[1]),set(all_[2])))*2)
    return answer