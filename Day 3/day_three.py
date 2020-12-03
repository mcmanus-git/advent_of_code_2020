# Part One

with open('input.txt') as file:
    txt = file.read().splitlines()


width = len(txt[0])
trees = 0
right = 0
for line in txt:
    if right >= width:
        right = right - width
        if line[right] == '#':
            trees += 1

    elif line[right] == '#':
        trees += 1

    right += 3

print(trees)


# Part Two
import math


def get_trees(mv_right, down, input_txt):
    """
    This function takes in required movements for a person on a toboggan which is heading down a hill.  The object
    is to determine how many trees they will encounter on their way down the hill which are indicated as '#' in the
    input txt file.

    :param mv_right: How many right moves the skier should move
    :param down: How many downward moves the skier should move
    :param input_txt: The input text file which contains the map of the toboggan slope
    :return: Int indicating how many trees the toboggan rider will encounter on the hill given the movement params
    """

    width = len(input_txt[0])
    trees = 0
    right = 0

    indexes = [line for line in range(0, len(input_txt), down)]
    # print(indexes)
    for index in indexes:
        if right >= width:
            right = right - width
            if input_txt[index][right] == '#':
                trees += 1

        elif input_txt[index][right] == '#':
            trees += 1

        right = right + mv_right

    return trees


with open('input.txt') as file:
    txt = file.read().splitlines()

print(math.prod([get_trees(r, d, txt) for r, d in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2])]))
