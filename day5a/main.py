
file = open("input.txt", "r")

f = file.read().split("\n")

seeds_start = f[0].find(":") + 2
seeds = list(map(lambda x: int(x), f[0][seeds_start:].split(" ")))
print(seeds)

fertilizer_to_water = []
with open("fertilizer-to-water") as fi:
    for line in fi:
        fertilizer_to_water.append(list(map(lambda x: int(x), line.split(" "))))

humidity_to_location = []
with open("humidity-to-location") as fi:
    for line in fi:
        humidity_to_location.append(list(map(lambda x: int(x), line.split(" "))))

light_to_temperature = []
with open("light-to-temperature") as fi:
    for line in fi:
        light_to_temperature.append(list(map(lambda x: int(x), line.split(" "))))

seed_to_soil = []
with open("seed-to-soil") as fi:
    for line in fi:
        seed_to_soil.append(list(map(lambda x: int(x), line.split(" "))))
soil_to_fertilizer = []
with open("soil-to-fertilizer") as fi:
    for line in fi:
        soil_to_fertilizer.append(list(map(lambda x: int(x), line.split(" "))))
temperature_to_humidity = []
with open("temperature-to-humidity") as fi:
    for line in fi:
        temperature_to_humidity.append(list(map(lambda x: int(x), line.split(" "))))
water_to_light = []
with open("water-to-light") as fi:
    for line in fi:
        water_to_light.append(list(map(lambda x: int(x), line.split(" "))))

# m is array of triples
def get_other(m, s):
    for a, b, c in m:
        if b <= s and s < b + c:
            return a + (s - b)
    return s


def intersection(s1, e1, s2, e2):
    if e1 < s2 or e2 < s1:
        return None
    return [max(s1, s2), min(e1, e2)]

def is_valid_interval(interval):
    return interval[0] < interval[1]

def find_location(maps, start, end):
    # padd = (7 - len(maps)) * " "
    if len(maps) == 0:
        return start
    intervals = [(start, end)]
    curr_map = maps[0]
    result = 9999999999999999999
    for a, b, c in curr_map:
        for itv in intervals:
            intersec = intersection(itv[0], itv[1], b, b + c)
            if intersec is not None:
                left = (itv[0], intersec[0] - 1)
                right = (intersec[1] + 1, itv[1])
                mapped_start = a + (intersec[0] - b)
                mapped_end = a + (intersec[1] - b)
                # print(padd, a,b,c, f"({intersec[0]}, {intersec[1]}) -> ({mapped_start}, {mapped_end})")
                if is_valid_interval(left):
                    intervals.append(left)
                if is_valid_interval(right):
                    intervals.append(right)
                locs = find_location(maps[1:], mapped_start, mapped_end)
                # print(padd, "LOCS", locs, mapped_start, mapped_end)
                result = min(result, locs)
                intervals.remove(itv)
                break
    
    # anything left over
    for itv in intervals:
        # print("LEFTOVER", itv)
        locs = find_location(maps[1:], itv[0], itv[1])
        result = min(result, locs)

    return result



        


# def find_location(s):
#     print("SDFLSDKFJLKSDJFLKSDJFLKDSJFLKSDJFLSDKJFLSDKJFLKSDJFLK")
#     soil = get_other(seed_to_soil, s)
#     print(soil)
#     fertilizer = get_other(soil_to_fertilizer, soil)
#     print(fertilizer)
#     water = get_other(fertilizer_to_water, fertilizer)
#     print(water)
#     light = get_other(water_to_light, water)
#     print(light)
#     temperature = get_other(light_to_temperature, light)
#     print(temperature)
#     humidity = get_other(temperature_to_humidity, temperature)
#     print(humidity)
#     location = get_other(humidity_to_location, humidity)
#     print(location)
#     return location



result = 9999999999999999
all_maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
for i in range(0, len(seeds), 2):
    l = find_location(all_maps, seeds[i], seeds[i] + seeds[i + 1] - 1)
    print(l)
    result = min(result, l)

print(result)

file.close()
