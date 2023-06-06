num = int(input())
time_ = list(map(int, input().split()))

time_ = sorted(time_)
local_wait = 0
global_wait = 0
for i in time_:
  local_wait = local_wait+i
  global_wait = global_wait+local_wait
print(global_wait)