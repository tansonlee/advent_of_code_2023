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
    
    new_rules[name] = (new_rule_list, rule_list[-1])

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

def should_accept(part):
    current_rule = "in"

    while True:
        print(current_rule)
        rule_set = rules[current_rule]
        matched = False
        for rule in rule_set[0]:
            part_val = part[rule[0]]
            other_val = rule[2]
            print(rule, part_val, other_val)
            if rule[1] == "<":
                if part_val < other_val:
                    current_rule = rule[3]
                    matched = True
                    break
            if rule[1] == ">":
                if part_val > other_val:
                    current_rule = rule[3]
                    matched = True
                    break
                
        if not matched:
            current_rule = rule_set[1]
        
        if current_rule == "R":
            return False
        if current_rule == "A":
            return True


result = 0
for part in parts:
    accept = should_accept(part)
    if accept:
        for c in part:
            result += part[c]


print(result)