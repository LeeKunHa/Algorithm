def solution(arr):
    row = len(arr)
    col = len(arr[0])
    if row>col:
        arr = [x+([0]*(row-col)) for x in arr]
    elif col>row:
        for i in range(col-row):
            arr.append([0]*(col))
    return arr