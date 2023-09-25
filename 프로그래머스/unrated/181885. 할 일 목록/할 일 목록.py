def solution(todo_list, finished):
    answer = [x for x,y in zip(todo_list,finished) if y==False]
    return answer