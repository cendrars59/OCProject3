def build_grid_from_file(file):
    grid = []
    with open(file, "r") as f:

        for line in f:
            row = []
            for c in line[:-1]:
                row.append(c)
            grid.append(row)

        return grid

def control_file(file):

    pass