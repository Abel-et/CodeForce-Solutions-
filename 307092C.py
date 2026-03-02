a,b = map(int, input().split())
arr1 =list(map(int, input().split()))
arr2 = list(map(int, input().split()))

cnt =0

i ,j = 0,0

while i < a and j < b:
  if arr1[i] < arr2[j]:
    i +=1
  elif arr1[i] > arr2[j]:
    j +=1
  else:
    current = arr1[i]
    count_a = 0
    
    while i < a and current == arr1[i]:
      count_a +=1
      i+=1
    
    count_b = 0
    while j < b and current == arr2[j]:
      j+=1
      count_b +=1
    cnt += count_b*count_a
print(cnt)