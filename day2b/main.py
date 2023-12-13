
def get_maxes(line):
    max_red = 0
    max_green = 0
    max_blue = 0
    start = line.find(":") + 1
    sets = line[start:].split(";")

    for s in sets:
        picks = s.split(",")
        for p in picks:
            p = p.strip()
            count, color = p.split(" ")
            count = int(count)
            if color == "red":
                max_red = max(max_red, count)
            elif color == "green":
                max_green = max(max_green, count)
            elif color == "blue":
                max_blue = max(max_blue, count)
    
    return max_red * max_green * max_blue


def main():
    result = 0
    with open("input.txt") as f:
        for line in f:
            result += get_maxes(line)
    print(result)


    

main()