n , m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int , input().split()))

pointer_1 , pointer_2 = 0, 0
merged = [] 

while pointer_1 < len(arr1) and pointer_2 < len(arr2):
  if arr1[pointer_1] >= arr2[pointer_2]:
    merged.append(arr2[pointer_2])
    pointer_2 +=1
  else:
    merged.append(arr1[pointer_1])
    pointer_1 +=1

merged.extend(arr2[pointer_2:])
merged.extend(arr1[pointer_1:])
print(*merged)