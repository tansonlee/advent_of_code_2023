
def is_possible(line):
    start = line.find(":") + 1
    sets = line[start:].split(";")
    print(sets)

    for s in sets:
        picks = s.split(",")
        for p in picks:
            p = p.strip()
            count, color = p.split(" ")
            count = int(count)
            if color == "red" and count > 12:
                return False
            elif color == "green" and count > 13:
                return False
            elif color == "blue" and count > 14:
                return False
    
    return True


def get_game_id(line):
    start = line.find(" ") + 1
    end = line.find(":")
    return int(line[start:end])


def main():
    result = 0
    with open("input.txt") as f:
        for line in f:
            possible = is_possible(line)
            if possible:
                game_id = get_game_id(line)
                result += game_id
                print(game_id, "possible")
    print(result)


    

main()