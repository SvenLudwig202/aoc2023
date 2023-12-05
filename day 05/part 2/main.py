import os
import re

path = os.path.dirname(os.path.realpath(__file__))
input = ""
sum = 0

maps = {}
seedlocations = {}

currentmap = ""

def lookupvalue(map, num):
    mapping = maps[map]
    
    for (m, v) in mapping.items():
        if num >= m and num <= v["destmax"]:
            diff = num - m
            # print("Map: {}, Num: {}, Min: {}, Max: {}, Source: {}, Diff: {}".format(map, num, m, v["destmax"], v["source"], diff))
            
            return v["source"] + diff
    
    return num

def lookupseedlocation(seed):
    soil = lookupvalue("seed-to-soil", seed)
    fertilizer = lookupvalue("soil-to-fertilizer", soil)
    water = lookupvalue("fertilizer-to-water", fertilizer)
    light = lookupvalue("water-to-light", water)
    temperature = lookupvalue("light-to-temperature", light)
    humidity = lookupvalue("temperature-to-humidity", temperature)
    location = lookupvalue("humidity-to-location", humidity)
    
    return location

with open(os.path.join(path,'input.txt')) as f:
    lines = f.readlines()


for line in lines:
    line = line.strip()

    # print(line)
    
    if line.startswith("seeds:"):
        matches = re.findall("(\d+)\s(\d+)", line)
        maps["seeds"] = {}
        
        for s in matches:
            maps["seeds"].update({
                    s[0]: s[1]
                })
    elif "map:" in line:
        matches = re.match("([\w\-]+)\smap:", line)
        currentmap = matches.group(1)
        maps[currentmap] = {}
        print("Processing {}".format(currentmap))
    elif line == "":
        print("")
        pass
    else:
        matches = re.findall("(\d+)", line)
        print(".", end="")
        
        maps[currentmap].update({
            int(matches[1]): {
                "destmax": int(matches[1]) + int(matches[2]),
                "source": int(matches[0])
            }
        })
        
        print(":", end="")

print("")
print("---")

for (s, v) in maps["seeds"].items():
    print("Processing Seeds starting at {} ({})".format(s, v))
    for i in range(int(s), int(s) + int(v) + 1):
        seedlocation = lookupseedlocation(int(i))
        # print("Seed: {}, Location: {}".format(i, seedlocation))
        seedlocations.update({i: seedlocation})

lowestseed = min(seedlocations, key=seedlocations.get)

print("---")
print("Lowest Seed: {}, Location: {}".format(lowestseed, seedlocations[lowestseed]))
# print('final sum: ' + str(sum))