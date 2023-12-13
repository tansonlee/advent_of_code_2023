f = open("input", "r")

data = f.read().split("\n")

def next_num(nums):
    if nums.count(0) == len(nums):
        return 0

    diffs = []
    for i in range(len(nums) - 1):
        diffs.append(nums[i+1] - nums[i])
    nxt = next_num(diffs)
    return nums[-1] + nxt


def prev_num(nums):
    if nums.count(0) == len(nums):
        print(nums)
        return 0

    diffs = []
    for i in range(len(nums) - 1):
        diffs.append(nums[i+1] - nums[i])
    nxt = prev_num(diffs)
    print(nxt, diffs)
    return nums[0] - nxt

result = 0
for line in data:
    nums = list(map(int, line.split(" ")))
    a = prev_num(nums)
    print(a)
    result += a

print(result)

f.close()