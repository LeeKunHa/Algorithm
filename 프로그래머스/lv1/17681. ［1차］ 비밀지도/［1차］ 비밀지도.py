def solution(n, arr1, arr2):
    answer = []
    arr1 = ([('0'*(n-len(bin(x)[2:])))+bin(x)[2:] for x in arr1])
    arr2 = ([('0'*(n-len(bin(x)[2:])))+bin(x)[2:] for x in arr2])
    for a1,a2 in zip(arr1,arr2):
        temp = []
        for i in range(n):
            if (a1[i] == '1') or (a2[i] == '1'):
                temp.append('#')
            else:
                temp.append(' ')
        answer.append(''.join(temp))       
    return answer