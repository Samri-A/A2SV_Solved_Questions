mat = []

for _ in range(5):
    n =  list(map(int, input().split()))
    mat.append(n)


for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 1:
            row = i
            col = j



moves = abs(row - 2) + abs(col - 2)
print(moves)

