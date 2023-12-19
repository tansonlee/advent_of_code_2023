import os
import inspect

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "test"), "r") as f:
    ops = [
        (d, int(a), c[2:-1])
        for d, a, c in [line.split() for line in f.read().splitlines()]
    ]


def get_pos(direction):
    match direction:
        case "R":
            return 1
        case "L":
            return -1
        case "U":
            return -1j
        case "D":
            return 1j



# part 2

curr_pos = 0
res = 0
total_a = 0

for _, _, h in ops:
    d, a = h[-1].translate(str.maketrans("0123", "RDLU")), int(h[:-1], 16)

    nxt = curr_pos + get_pos(d) * a
    res += curr_pos.real * nxt.imag
    res -= nxt.real * curr_pos.imag
    # res += a
    total_a += a
    curr_pos = nxt

print(int(res / 2) + (total_a / 2) + 1)