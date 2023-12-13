
file = open("i", "r")

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
        if a <= s and s < a + c:
            return b + (s - a)
    return s



def find_location(s):
    soil = get_other(seed_to_soil, s)
    fertilizer = get_other(soil_to_fertilizer, soil)
    water = get_other(fertilizer_to_water, fertilizer)
    light = get_other(water_to_light, water)
    temperature = get_other(light_to_temperature, light)
    humidity = get_other(temperature_to_humidity, temperature)
    location = get_other(humidity_to_location, humidity)
    return location



result = 9999999999999999
for s in seeds:
    l = find_location(s)
    result = min(result, l)

print(result)

file.close()
