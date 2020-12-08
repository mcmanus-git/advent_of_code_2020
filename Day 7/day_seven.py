import re

with open('input.txt') as file:
    data = file.readlines()

forward = {}
backward = {}

for line in data:
    (key, values) = line.split(" bags contain ")
    forward[key] = []
    if not (values.rstrip() == "no other bags."):
        for part in values.split(','):
            new = part.split(" bags")[0]
            new2 = re.search("(\d+)\s(\w+\s\w+)", new).groups()
            forward[key].append(new2)
            if new2[1] not in backward:
                backward[new2[1]] = []
            backward[new2[1]].append(key)


def find_containers(parent, backward):
    if parent in backward.keys():
        parents = backward[parent]
        bv = set()
        backward.pop(parent)
        for prnt in parents:
            bv.add(prnt)
            for val in find_containers(prnt, backward):
                bv.add(val)
        return bv
    else:
        return set()


# Part Two
def inside_count(bag_color, forward, num):
    count = 0
    for bag in forward[bag_color]:
        count += int(bag[0]) * num
        count += inside_count(bag[1], forward, int(bag[0]) * num)
    return count


part1 = len(find_containers("shiny gold", backward))
part2 = inside_count("shiny gold", forward, 1)

print(f"Part One: {part1}\n Part Two: {part2}")
