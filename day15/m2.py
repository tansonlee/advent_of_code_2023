f = open("real", "r")
data = f.read().split(",")
# data = [list(x) for x in data]

def h(s):
    result = 0
    for char in s:
        result += ord(char)
        result *= 17
        result %= 256
    return result

boxes = [[] for _ in range(256)]

for x in data:
    op_index = max(x.find("-"), x.find("="))
    label = x[:op_index]

    hsh = h(label)

    if x[op_index] == "-":
        for l in boxes[hsh]:
            if l[0] == label:
                boxes[hsh].remove(l)
                break
    if x[op_index] == "=":
        focal_length = int(x[op_index + 1])
        found = False
        for l in boxes[hsh]:
            if l[0] == label:
                found = True
                l[1] = focal_length
                break
        
        if not found:
            boxes[hsh].append([label, focal_length])


result = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        result += (i + 1) * (j + 1) * boxes[i][j][1]

print(result)


f.close()

