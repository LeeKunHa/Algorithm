num_A = int(input())
num_B = int(input())
num_C = int(input())

result = str(num_A * num_B * num_C)
for i in range(10):
    print(result.count(str(i)))