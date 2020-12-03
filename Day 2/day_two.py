# Part One

# import pandas as pd
# import re
#
# # Where the input came from https://adventofcode.com/2020/day/2/input
# txt = pd.read_csv('input.txt', header=None)[0].values
#
#
# valid_passwords = []
# pattern = '(?P<min>\d{1,2})[-](?P<max>\d{1,2})[ ](?P<letter>\w)[:][\s](?P<password>\w*)'
# # m_dict = match.groupdict()
# # minimum = int(m_dict['min'])
# # maximum = int(m_dict['max'])
#
#
# for string in txt:
#     match = re.match(pattern, string)
#     m_dict = match.groupdict()
#     minimum = int(m_dict['min'])
#     maximum = int(m_dict['max'])
#     letter_count = match.groupdict()['password'].count(match.groupdict()['letter'])
#     if maximum >= letter_count >= minimum:
#         valid_passwords.append(string)
#
# print(len(valid_passwords))

# Part Two

# import pandas as pd
# import re
#
# # Where the input came from https://adventofcode.com/2020/day/2/input
# txt = pd.read_csv('input.txt', header=None)[0].values
#
#
# valid_passwords = []
# pattern = '(?P<min>\d{1,2})[-](?P<max>\d{1,2})[ ](?P<letter>\w)[:][\s](?P<password>\w*)'
# # m_dict = match.groupdict()
# # minimum = int(m_dict['min'])
# # maximum = int(m_dict['max'])
#
#
# for string in txt:
#     match = re.match(pattern, string)
#     m_dict = match.groupdict()
#     minimum = int(m_dict['min']) - 1
#     maximum = int(m_dict['max']) - 1
#     letter = m_dict['letter']
#     password = m_dict['password']
#
#     if password[minimum] == letter and password[maximum] == letter:
#         next
#     elif password[minimum] != letter and password[maximum] != letter:
#         next
#     else:
#         valid_passwords.append(string)
#
# print(len(valid_passwords))


# BOTH PARTS
import pandas as pd
import re

# Where the input came from https://adventofcode.com/2020/day/2/input
txt = pd.read_csv('input.txt', header=None)[0].values


def valid_passwords(passwords, part):

    valid_passwords = []
    pattern = '(?P<min>\d{1,2})[-](?P<max>\d{1,2})[ ](?P<letter>\w)[:][\s](?P<password>\w*)'

    if part == 1:
        for string in txt:
            match = re.match(pattern, string)
            m_dict = match.groupdict()
            minimum = int(m_dict['min'])
            maximum = int(m_dict['max'])
            letter_count = match.groupdict()['password'].count(match.groupdict()['letter'])
            if maximum >= letter_count >= minimum:
                valid_passwords.append(string)
        return len(valid_passwords)

    if part == 2:
        for string in txt:
            match = re.match(pattern, string)
            m_dict = match.groupdict()
            minimum = int(m_dict['min']) - 1
            maximum = int(m_dict['max']) - 1
            letter = m_dict['letter']
            password = m_dict['password']

            if password[minimum] == letter and password[maximum] == letter:
                next
            elif password[minimum] != letter and password[maximum] != letter:
                next
            else:
                valid_passwords.append(string)

        return len(valid_passwords)


psswrds1 = valid_passwords(txt, 1)
psswrds2 = valid_passwords(txt, 2)


print(psswrds1, psswrds2)
