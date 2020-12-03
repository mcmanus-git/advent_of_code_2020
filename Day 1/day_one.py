import pandas as pd
import numpy as np
from itertools import combinations

# Where the input came from https://adventofcode.com/2020/day/1/input
txt = pd.read_csv('day_1_input.txt', header=None)[0].values



def find_pairs(nums_list, desired_sum, num_pairs):
    return np.prod([pair for pair in combinations(nums_list, num_pairs) if sum(pair) == desired_sum])


pairs = find_pairs(txt, 2020, 3)


print(pairs)