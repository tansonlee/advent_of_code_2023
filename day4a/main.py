
def main():
    result = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            start = line.find(":") + 1
            win, have = line[start:].split("|")
            win.strip()
            have.strip()
            win = win.split(" ")
            have = have.split(" ")

            print("wh", win, have)

            score = 0
            for w in win:
                if w == '':
                    continue
                if w in have:
                    if score == 0:
                        score = 1
                    else:
                        score *= 2
            print(score)
            result += score
    
    print(result)




main()