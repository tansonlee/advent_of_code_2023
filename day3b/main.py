
def main():
    with open("input.txt") as f:
        data = f.read().split("\n")
        gears = {}
        for row, line in enumerate(data):
            i = 0
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
                            if data[x][y] == "*":
                                if (x,y) not in gears:
                                    gears[(x,y)] = []
                                gears[(x,y)].append(int(line[start:end]))
                else:
                    i += 1
        result = 0
        for ge in gears:
            g = gears[ge]


            if len(g) == 2:
                result += (g[0] * g[1])
        
        print(gears)
        print(result)
        

                    



main()