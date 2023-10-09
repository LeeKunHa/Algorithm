def solution(n, k):
    string = ''
    while n!=0:
        string=string+str(n%k)
        n = (n//k)
    string = [x for x in str(string)[::-1].split('0') if x]
    answer = len([x for x in string if is_prime(int(x))])
    return answer

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True