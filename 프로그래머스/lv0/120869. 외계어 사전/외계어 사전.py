def solution(spell, dic):
    for word in dic:
        word_ = []
        for c in word:
            word_.append(c)
            if set(word_) == set(spell):
                answer = 1
                return answer
    return 2