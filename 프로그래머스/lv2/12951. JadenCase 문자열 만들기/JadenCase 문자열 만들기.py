"""
def solution(s):
    str_list = [x.capitalize() for x in s.split()]
    for i in range(len(str_list)):
        s = s.replace(s.split()[i],str_list[i])
    answer = s
    return answer
"""

def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer