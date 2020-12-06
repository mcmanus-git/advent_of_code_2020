# Part One Original:
data = [i.split() for i in open('input.txt', 'r').read().split('\n\n')]

sums = []
for group in data:
    sums.append(len(set("".join(group))))
print(sum(sums))

# Part One Tweaked:
print(sum([len(set("".join(group))) for group in [i.split() for i in open('input.txt', 'r').read().split('\n\n')]]))

# Part Two Original:
import collections
counts = []
for group in data:
    frequencies = collections.Counter("".join(group))
    counts.append(len([i for i in frequencies.values() if i == len(group)]))
print(sum(counts))

# Part Two Tweaked:
import collections
print(sum([len([i for i in collections.Counter("".join(group)).values() if i == len(group)]) for group in [i.split() for i in open('input.txt', 'r').read().split('\n\n')]]))

