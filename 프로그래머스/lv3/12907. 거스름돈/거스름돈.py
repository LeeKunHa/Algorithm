def solution(n, money):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in money:
        for j in range(i,n+1):
            dp[j] += dp[j-i] 
    answer = dp[n]%1000000007
    return answer