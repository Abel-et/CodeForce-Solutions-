test = int(input())

for i in range(test):
  s = input()
  if len(s)<2:
    if int(s[0]) < int(s[1]):
      print(f'{s[0]} {s[1]}')
      continue
    else:
      print(-1)
  for i in range(1,len(s)):
    left =s[:i]
    right = s[i:]
    if right[0] == '0':
      continue
    elif int(left) < int(right):
      print(f'{left} {right}')
      break
  else:
    print(-1)