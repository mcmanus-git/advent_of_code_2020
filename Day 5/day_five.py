with open('input.txt') as file:
    txt = file.read().splitlines()

# Part One
seat_id_list = []
for line in txt:

    row_max = 128
    row_min = 0
    col_max = 8
    col_min = 0

    for char in line:
        if char == 'F':
            row_max = (row_max + row_min) / 2
        if char == 'B':
            row_min = (row_max + row_min) / 2
        if char == 'L':
            col_max = (col_max + col_min) / 2
        if char == 'R':
            col_min = (col_max + col_min) / 2

    seat_id = row_min * 8 + col_min
    seat_id_list.append(seat_id)

seat_id_list.sort()
print(seat_id_list[-1])

# Part Two

print([num for num in [i for i in range(35, 886)] if num not in seat_id_list])
