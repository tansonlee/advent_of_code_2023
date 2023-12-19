f = open("in", "r")

data = f.read().split("\n")
data = [list(x) for x in data]


def transform(data):
    for col in range(len(data[0])):
        for row in range(1, len(data)):
            if data[row][col] == "O":
                data[row][col] = "."
                for new_row in reversed(range(row)):
                    if data[new_row][col] in "#O":
                        data[new_row + 1][col] = "O"
                        break
                    if new_row == 0:
                        data[0][col] = 'O'
    
def col_load(col):
    res = 0
    for row in range(len(data)):
        if data[row][col] == "O":
            res += len(data) - row
    
    return res


def pp(arr):
    for x in arr:
        print(*x)

result = 0

transform(data)
pp(data)

for col in range(len(data[0])):
    for row in range(len(data)):
        if data[row][col] == "O":
            print(row, col, data[row][col], len(data) - row)
            result += len(data) - row
    # a = col_load(col)
    # print(col, a)
    # result += a

print(result)
f.close()
