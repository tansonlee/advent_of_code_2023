
def digit_at(str, i):
    if str[i].isdigit():
        return int(str[i])
    
    mp = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    for n in mp:
        if str[i:i+len(n)] == n:
            return mp[n]

    return -1

def get_value(s):
    first_num = -1
    for i in range(len(s)):
        x = digit_at(s, i)
        if x != -1:
            first_num = x
            break

    last_num = -1
    for i in reversed(range(len(s))):
        x = digit_at(s, i)
        if x != -1:
            last_num = x
            break
    
    return int(str(first_num) + str(last_num))


def main():
    result = 0
    with open("input2.txt") as f:
        for line in f:
            value = get_value(line)
            result += value
    print(result)


main()