str = input()
answer = ''
for i in str:
    if i == i.lower():
        answer=answer+i.upper()
    else:
        answer=answer+i.lower()
print(answer)