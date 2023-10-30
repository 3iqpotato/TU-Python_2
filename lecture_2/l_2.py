data = [-1, 10, 11, -32, 15]
print(data)
data.sort(key=lambda x: -x)
print(data)

data = [[1, 2, 3],
        [4, 5,]]

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=' ')
    print()

data = [[123, 'Ivan', 5.65],
        [222, 'Peter', 5.33],
        [333, 'Lili', 5.45]]

print(data)
data.sort(key=lambda st: st[2])
print(data)

