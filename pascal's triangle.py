n = int(input("Enter number of rows: "))
a = []
for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = a[i - 1][j - 1] + a[i - 1][j]
    a.append(row)  # <-- append the row

for row in a:      # <-- print after building all rows
    print(' '.join(map(str, row)))