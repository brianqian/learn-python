def get_value_from_range(source: str, dest: str, range: str, seed_key: str):
    source, dest, range, seed_key = int(source), int(dest), int(range), int(seed_key)
    if seed_key < source or seed_key >= source + range:
        return seed_key
    else:
        return dest + seed_key - source


with open("./input.txt") as f:
    seeds = []
    modified_idxs = set()
    for line in f:
        line = line.rstrip("\n")
        if line.endswith(":") or line == "":
            modified_idxs.clear()
            print(line, seeds)
            continue
        if line.startswith("seeds: "):
            seeds = line.split(" ")[1:]
            continue

        dest, source, range = line.split(" ")
        for idx, num in enumerate(seeds):
            if idx in modified_idxs:
                continue
            res = get_value_from_range(source, dest, range, num)
            if res != num:
                modified_idxs.add(idx)
                seeds[idx] = res
    print(seeds, min(seeds))

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
 
# using zip() to map values
mapped = zip(name, roll_no)
 
print(set(mapped))