

def solution(name):
    up_down = 0
    left_right = len(name)-1
    answer=0
    for i,x in enumerate(name):
        up_down = up_down+min(ord(x)-ord('A'),ord('Z')-ord(x)+1)
        
        next_ = i+1
        while next_<len(name) and name[next_]=='A':
            next_ = next_+1        
        left_right = min([left_right,(i*2+len(name)-next_),((len(name)-next_)*2+i)])
    answer = answer+up_down+left_right
    return answer