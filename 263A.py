
for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        r = i + 1          # row index 
        c = row.index(1) + 1  # column index 

moves = abs(r - 3) + abs(c - 3)
print(moves)