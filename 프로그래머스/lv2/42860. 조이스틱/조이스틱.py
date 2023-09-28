def solution(name):
    up_down = 0
    left_right = len(name)-1
    for i in range(len(name)):
        up_down = up_down + min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
        
        next_ = i+1
        while next_ < len(name) and name[next_]=='A':
            next_ = next_+1
        left_right = min([left_right, 2*i+(len(name)-next_), 2*(len(name)-next_)+i])
    answer = up_down + left_right
    return answer