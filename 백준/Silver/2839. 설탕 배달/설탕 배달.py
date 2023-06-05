num = int(input())

small_3 = 0
while num >= 0:
  if num % 5 == 0:
    big_5 = num//5
    break
  else:
    num = num-3
    small_3 += 1

if num < 0:
  print(-1)
else:
  print(big_5+small_3)