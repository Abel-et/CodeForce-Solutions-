n , k  = map(int,input().split())
score = [int(num) for num in input().split()]
contest = score[k-1]
total = 0

for i in score:
  if i >= contest and i > 0:
    total +=1
print(total)