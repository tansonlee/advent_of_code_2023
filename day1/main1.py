
def get_value(str):
    first_num = -1
    for i in str:
        if i.isdigit():
            first_num = i
            break
    
    last_num = -1
    for i in str[::-1]:
        if i.isdigit():
            last_num = i
            break
    
    return int(first_num + last_num)


def main():
    result = 0
    with open("input1.txt") as f:
        for line in f:
            value = get_value(line)
            result += value
    print(result)


main()