from functools import cache

f = open("input", "r")
data = f.read().split("\n")
# data = [list(x) for x in f.read().split("\n")]

def pretty_print(a):
    for x in a:
        print(x)

parsed = []
for line in data:
    records, nums = line.split(" ")
    records = "?".join([records for _ in range(5)])
    nums = [int(x) for x in nums.split(",")]
    nums = tuple(nums + nums + nums + nums + nums)
    parsed.append((records, nums))


pretty_print(parsed)



@cache
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

for a, b in enumerate(parsed):
    records = b[0]
    nums = b[1]
    x = find_ways(records, nums)
    result += x
    print(x, records, nums)
    print("PERCENT", a / len(parsed) * 100)

print(result)


f.close()