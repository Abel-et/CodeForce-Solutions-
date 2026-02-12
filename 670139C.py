size = int(input())
arr = list(map(int, input().split()))

solution =sorted(arr ,reverse=True)
ans = {}

position  = 0
if len(arr) <2:
  print(arr[0])
else:
  for i in range(1,len(solution)):
    if solution[i] == solution[i-1]:
      p = solution[i]
      if p not in ans:
        ans[p] = position
      position +=2
    elif solution[i] <solution[i-1]:
      ans[solution[i]] = position
      position +=1

  final = []
  for i in arr:
    current = ans[i]
    final.append(current)
  print(*final)