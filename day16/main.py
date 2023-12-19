f = open("real", "r")
data = f.read().split("\n")
data = [list(x) for x in data]
f.close()

total_cols = len(data[0])
total_rows = len(data)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def pp(a):
    for x in a:
        print(*x)

def get_energized(start_row, start_col, start_dir):
    energized = [[0 for _ in range(total_cols)] for _ in range(total_rows)]

    # of tuples (row, col, direction)
    beams = [(start_row, start_col, start_dir)]
    visited = set()

    while len(beams) > 0:
        row, col, direction = beams.pop(0)
        if row < 0 or row >= total_rows or col < 0 or col >= total_cols:
            continue
        if (row, col, direction) in visited:
            continue
        visited.add((row, col, direction))
        energized[row][col] = 1

        if data[row][col] == "/":
            if direction == UP:
                beams.append((row, col + 1, RIGHT))
            elif direction == RIGHT:
                beams.append((row - 1, col, UP))
            elif direction == DOWN:
                beams.append((row, col - 1, LEFT))
            elif direction == LEFT:
                beams.append((row + 1, col, DOWN))
        elif data[row][col] == "\\":
            if direction == UP:
                beams.append((row, col - 1, LEFT))
            elif direction == RIGHT:
                beams.append((row + 1, col, DOWN))
            elif direction == DOWN:
                beams.append((row, col + 1, RIGHT))
            elif direction == LEFT:
                beams.append((row - 1, col, UP))
        elif data[row][col] == "|":
            if direction == UP:
                beams.append((row - 1, col, direction))
            elif direction == RIGHT:
                beams.append((row + 1, col, DOWN))
                beams.append((row - 1, col, UP))
            elif direction == DOWN:
                beams.append((row + 1, col, direction))
            elif direction == LEFT:
                beams.append((row + 1, col, DOWN))
                beams.append((row - 1, col, UP))
        elif data[row][col] == "-":
            if direction == UP:
                beams.append((row, col - 1, LEFT))
                beams.append((row, col + 1, RIGHT))
            elif direction == RIGHT:
                beams.append((row, col + 1, direction))
            elif direction == DOWN:
                beams.append((row, col - 1, LEFT))
                beams.append((row, col + 1, RIGHT))
            elif direction == LEFT:
                beams.append((row, col - 1, direction))
        elif data[row][col] == ".":
            if direction == UP:
                row = row - 1
            elif direction == RIGHT:
                col = col + 1
            elif direction == DOWN:
                row = row + 1
            elif direction == LEFT:
                col = col - 1
            beams.append((row, col, direction))
        else:
            print("BAD SQUARE")



    result = 0
    for row in range(total_rows):
        for col in range(total_cols):
            if energized[row][col] == 1:
                result += 1
    
    return result


result = 0
for i in range(total_rows):
    result = max(result, get_energized(i, 0, RIGHT))
    result = max(result, get_energized(i, total_cols - 1, LEFT))
for i in range(total_cols):
    result = max(result, get_energized(0, i, DOWN))
    result = max(result, get_energized(total_rows - 1, i, UP))


print(result)


