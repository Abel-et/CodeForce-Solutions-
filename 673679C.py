n  = int(input())

w , h = map(int,input().split())
prev_height = max(w,h)

for i in range(n-1):
  w , h = map(int,input().split())
  curr_max = max(w,h)
  curr_min = min(w,h)
  
  if curr_max <= prev_height:
    prev_height = curr_max
  elif curr_min <= prev_height:
    prev_height = curr_min
  else:
    print('NO')
    break
else:
  print("YES")
