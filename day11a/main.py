f = open("input", "r")
data = f.read().split("\n")
# data = [list(x) for x in f.read().split("\n")]

def pretty_print(a):
    for x in a:
        print(x)

parsed = []
for line in data:
    records, nums = line.split(" ")
    nums = [int(x) for x in nums.split(",")]
    parsed.append((records, nums))


pretty_print(parsed)



def find_ways(r, n):
    if r == "" and len(n) != 0:
        return 0
    if len(n) == 0 and r.count("#") > 0:
        return 0
    if len(n) == 0:
        return 1

    curr = n[0]
    if r[0] == "?":
        # if there are n[0] ? in a row
        if r[:curr].count("?") + r[:curr].count("#") == curr:
            if len(r) > curr and r[curr] == "#":
                return find_ways(r[1:], n)
            # print("x", r[:curr], r[:curr].count("?"), r[:curr].count("#"))
            # print("---", r, n, find_ways_np(r[curr + 1:], n[1:]), find_ways_np(r[1:], n))
            return find_ways(r[curr + 1:], n[1:]) + find_ways(r[1:], n)
    if r[0] == "#":
        if r[:curr].count("?") + r[:curr].count("#") == curr:
            if len(r) > curr and r[curr] == "#":
                return 0
            # print("y", r[:curr])
            return find_ways(r[curr + 1:], n[1:])
        else:
            return 0
    return find_ways(r[1:], n)

result = 0

for records, nums in parsed:
    x = find_ways(records, nums)
    print(x, records, nums)
    result += x

print(result)


f.close()