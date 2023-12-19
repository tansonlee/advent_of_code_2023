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


result = 0
for x in data:
    a = h(x)
    result += a

print(result)


f.close()

