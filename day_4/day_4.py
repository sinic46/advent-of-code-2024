def get_input():
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        return lines


def check_for_matches(data, check_char):
    matches = 0

    for vert_idx, line in enumerate(data):
        for hor_idx, value in enumerate(line):
            if value == check_char:
                matches += get_check_grid_2_mas(data, vert_idx, hor_idx)

    return matches


def get_check_grid_xmas(data, vert_index, hor_index):

    match_count = 0

    grid_width = len(data[0])
    grid_w_min = grid_width - 2
    grid_hieght = len(data)
    grid_h_min = grid_hieght - 2

    if hor_index < grid_w_min:

        # normal
        if data[vert_index][hor_index+1] == 'M' and data[vert_index][hor_index+2] == 'A' and data[vert_index][hor_index+3] == 'S':
            match_count += 1

        # diagonal down right
        if vert_index < grid_h_min:
            if data[vert_index+1][hor_index+1] == 'M' and data[vert_index+2][hor_index+2] == 'A' and data[vert_index+3][hor_index+3] == 'S':
                match_count += 1

            # diagonal up right
        if vert_index > 2:
            if data[vert_index-1][hor_index+1] == 'M' and data[vert_index-2][hor_index+2] == 'A' and data[vert_index-3][hor_index+3] == 'S':
                match_count += 1

    if hor_index > 2:

        # reverse
        if data[vert_index][hor_index-1] == 'M' and data[vert_index][hor_index-2] == 'A' and data[vert_index][hor_index-3] == 'S':
            match_count += 1

        # diagonal down left
        if vert_index < grid_h_min:
            if data[vert_index+1][hor_index-1] == 'M' and data[vert_index+2][hor_index-2] == 'A' and data[vert_index+3][hor_index-3] == 'S':
                match_count += 1

        # diagonal up left
        if vert_index > 2:
            if data[vert_index-1][hor_index-1] == 'M' and data[vert_index-2][hor_index-2] == 'A' and data[vert_index-3][hor_index-3] == 'S':
                match_count += 1

    # down
    if vert_index < grid_h_min:
        if data[vert_index+1][hor_index] == 'M' and data[vert_index+2][hor_index] == 'A' and data[vert_index+3][hor_index] == 'S':
            match_count += 1

    # up
    if vert_index > 2:
        if data[vert_index-1][hor_index] == 'M' and data[vert_index-2][hor_index] == 'A' and data[vert_index-3][hor_index] == 'S':
            match_count += 1

    return match_count


def get_check_grid_2_mas(data, vert_index, hor_index):

    match_count = 0

    grid_width = len(data[0])
    grid_w_min = grid_width - 2
    grid_hieght = len(data)
    grid_h_min = grid_hieght - 1


    if 0 < hor_index < grid_w_min and 0 < vert_index < grid_h_min:
        if data[vert_index+1][hor_index+1] in ['M', 'S'] and data[vert_index-1][hor_index-1] in ['M', 'S'] and data[vert_index+1][hor_index+1] != data[vert_index-1][hor_index-1]:
            if data[vert_index-1][hor_index+1] in ['M', 'S'] and data[vert_index+1][hor_index-1] in ['M', 'S'] and data[vert_index-1][hor_index+1] != data[vert_index+1][hor_index-1]:
                match_count += 1

    return match_count


if __name__ == '__main__':

    print(check_for_matches(get_input(), 'A'))
