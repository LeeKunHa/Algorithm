def solution(answers):
    answer = []
    index_ = [0,0,0]
    student_1 = [1, 2, 3, 4, 5]
    student_1 = student_1*(len(answers)//len(student_1)+1)
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_2 = student_2*(len(answers)//len(student_2)+1)
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    student_3 = student_3*(len(answers)//len(student_3)+1)
    for i in range(len(answers)):
        if answers[i] == student_1[i]:
            index_[0] = index_[0]+1
        if answers[i] == student_2[i]:
            index_[1] = index_[1]+1
        if answers[i] == student_3[i]:
            index_[2] = index_[2]+1
    for i in enumerate(index_):
        print(i)
        if i[1] == max(index_):
            answer.append(i[0]+1)
    return answer