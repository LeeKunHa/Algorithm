num = int(input())
time_ = list(map(int, input().split()))

time_ = sorted(time_)
global_wait = 0
total_wait = 0
for i in time_:
  global_wait = global_wait+i
  total_wait = total_wait+global_wait
print(total_wait)