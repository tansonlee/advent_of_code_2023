
# records = [(54, 302), (94, 1476), (65, 1029), (92, 1404)]
records = [(54946592, 302147610291404)]


result = 1
for time, distance in records:
    possibilities = 0
    for charge in range(time + 1):
        if charge * (time - charge) > distance:
            possibilities += 1
    result *= possibilities

print(result)
