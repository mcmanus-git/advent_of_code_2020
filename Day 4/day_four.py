# Part One

import pandas as pd
import numpy as np

lines_dict = {}
lines_list = []
count = 0
with open('input.txt') as file:
    txt = file.readlines()

for line in txt:
    lines_list.append(line)
    if line == '\n' or line == txt[-1]:
        count += 1
        val = ' '.join(lines_list).replace('\n', '').strip()
        val_dict = dict(item.split(":") for item in val.split(" "))
        lines_dict[count] = val_dict
        lines_list = []

df = pd.DataFrame(lines_dict).T

params = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

print(len(df[params].dropna()))


# Part Two

# Conditions

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


df = df[params]
df.dropna(inplace=True)


df['measure'] = df['hgt'].apply(lambda x: str(x)[-2:] if str(x)[-2:] == "cm" or str(x)[-2:] == "in" else np.nan)
df['hgt'] = df['hgt'].str.replace('\D', '').dropna().astype(int)
mes = df.where(((df['measure'] == 'cm') & (df['hgt'].between(150,193))) | ((df['measure'] == 'in') & (df['hgt'].between(59,76)))).dropna()

mes['byr'] = mes['byr'].dropna().astype(int)
mes['iyr'] = mes['iyr'].dropna().astype(int)
mes['eyr'] = mes['eyr'].dropna().astype(int)

print(len(mes.loc[(mes['byr'].between(1920, 2002)) & (mes['iyr'].between(2010, 2020)) &
                  (mes['eyr'].between(2020, 2030)) & (mes['hcl'].str.contains('(#[0-9a-f]{6}$)')) &
                  (mes['ecl'].str.contains('(^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$){1}')) &
                  (mes['pid'].str.contains('(^[0123456789]{9}$)'))]
          )
      )
