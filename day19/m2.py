import copy

f = open("real", "r")
data = f.read()
f.close() 
rules, parts = data.split("\n\n")

rules = rules.strip().split("\n")
parts = parts.strip().split("\n")

# parse the rules
new_rules = {}
for r in rules:
    open_curly = r.index("{")
    name = r[:open_curly]
    rule_list = r[open_curly + 1: -1].split(",")

    new_rule_list = []
    for x in rule_list[:-1]:
        category = x[0]
        cmp = x[1]
        colon = x.index(":")
        val = int(x[2:colon])
        next_rule = x[colon + 1:]
        new_rule_list.append((category, cmp, val, next_rule))
    new_rule_list.append(rule_list[-1])
    
    new_rules[name] = new_rule_list

rules = new_rules

# parse the parts
new_parts = []
for p in parts:
    pieces = p[1:-1].split(",")
    pt = {}
    for x in pieces:
        pt[x[0]] = int(x[2:])
    new_parts.append(pt)

parts = new_parts


print(rules)
print(parts)

def get_split_up(rule, part):
    # print(rule)
    curr_rule = rule[0]
    if len(rule) == 1:
        return [[curr_rule, part]]
    elif curr_rule[1] == "<":
        new_p1 = copy.deepcopy(part)
        new_p1[curr_rule[0]][1] = curr_rule[2] - 1
        new_r1 = curr_rule[3]

        new_p2 = copy.deepcopy(part)
        new_p2[curr_rule[0]][0] = curr_rule[2]
        rest = get_split_up(rule[1:], new_p2)
        return [[new_r1, new_p1]] + rest
    elif curr_rule[1] == ">":
        new_p1 = copy.deepcopy(part)
        new_p1[curr_rule[0]][0] = curr_rule[2] + 1
        new_r1 = curr_rule[3]

        new_p2 = copy.deepcopy(part)
        new_p2[curr_rule[0]][1] = curr_rule[2]
        rest = get_split_up(rule[1:], new_p2)
        return [[new_r1, new_p1]] + rest
    else:
        print("SOMETHING RLY BAD")

print(get_split_up(rules["in"], {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}))

def should_accept(rule, part):
    # print(rule)
    if rule == "R":
        return 0
    for c in part:
        if part[c][1] - part[c][0] + 1 <= 0:
            return 0
    if rule == "A":
        p = 1
        for c in part:
            p *= (part[c][1] - part[c][0] + 1)
        return p

    current_rule = rule
    rule_set = rules[current_rule]
    next_rules_and_parts = []

    next_rules_and_parts.extend(get_split_up(rule_set, part))
    
    result = 0
    for r, p in next_rules_and_parts:
        result += should_accept(r, p)

    return result



result = should_accept("in", {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]})

print(result)