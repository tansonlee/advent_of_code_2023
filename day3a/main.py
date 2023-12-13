
def main():
    with open("input.txt") as f:
        data = f.read().split("\n")
        result = 0
        for row, line in enumerate(data):
            i = 0
            print(line)
            while i < len(line):
                if line[i].isdigit():
                    start = i
                    # find the end of the number
                    while i < len(line) and line[i].isdigit():
                        i += 1
                    end = i
                    print(start, end, line[start:end])
                    
                    # do a search around this number
                    neighbors = []

                    # top
                    for col in range(start - 1, end + 1):
                        neighbors.append((row - 1, col))
                    #bottom
                    for col in range(start - 1, end + 1):
                        neighbors.append((row + 1, col))
                    
                    neighbors.append((row, start - 1))
                    neighbors.append((row, end))
                    print(neighbors)

                    for x, y in neighbors:
                        if x >= 0 and x < len(line) and y >= 0 and y < len(data):
                            if not (data[x][y].isdigit() or data[x][y] == "."):
                                print("SLDJFLKSDJFLKSDJLFK", line[start:end])
                                result += int(line[start:end])
                else:
                    i += 1
        
        print(result)

                    



main()