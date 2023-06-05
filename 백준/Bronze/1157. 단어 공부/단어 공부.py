text = input().upper()

text_dict = {}
for i in text:
  text_dict[i] = 0

count = 0
for i in text:
  max_ = max(text_dict.values())
  text_dict[i] = text_dict[i]+1
  if text_dict[i] == max(text_dict.values()):
    answer = i
    if max_ == max(text_dict.values()):
      answer = '?'
print(answer)