def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        count=0
        for j in range(1,int(i**0.5)+1):
            if(i%j==0):
                count=count+2
                if j**2==i: 
                    count=count-1
            if count>limit:
                count=power
                break
        answer = answer+count
    return answer