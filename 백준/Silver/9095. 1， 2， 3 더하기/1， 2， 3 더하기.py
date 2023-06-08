T = int(input())

dp = [0]*11
dp[1],dp[2],dp[3] = 1,2,4

def sum_case(n):
  for i in range(4,n+1):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
  return dp[n]

for i in range(T):
  N = int(input())
  print(sum_case(N))