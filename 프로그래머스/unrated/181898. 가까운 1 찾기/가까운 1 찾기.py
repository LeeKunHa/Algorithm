def solution(arr, idx):
    first = [i for i,x in enumerate(arr[idx:]) if x==1]
    if not first:
        answer = -1
    else:
        answer = first[0]+idx
    return answer