def solution(arr):
    try:
        start = ''.join(list(map(str,arr))).replace('10','0').index('2')
        end = ''.join(list(map(str,arr))).replace('10','0').rindex('2')
        answer = arr[start:end+1]
    except:
        return [-1]
    return answer