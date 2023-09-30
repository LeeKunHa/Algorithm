def solution(arr, queries):
    for i in queries:
        for j,x in enumerate(arr):
            if j>=i[0] and j<=i[1] and j%i[2]==0:
                arr[j]=arr[j]+1
    answer = arr
    return answer