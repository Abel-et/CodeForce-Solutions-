n , m = map(int , input().split())

arr1 = [*map(int, input().split())]
arr2 = [*map(int, input().split())]

count = []
first = 0

for second in range(len(arr2)):
  while first < len(arr1) and arr1[first] < arr2[second]:
    first +=1
  
  count.append(first)
print(*count)