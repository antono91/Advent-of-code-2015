def main():
    print(solve(parse_input('day18.in'), 100, True))
    print(solve(parse_input('day18.in'), 100, False))


def parse_input(file):
    grid = dict()
    with open('day18.in') as f:
        for i, line in enumerate(f.readlines()):
            for j, c in enumerate(line.strip()):
                grid[(i, j)] = c
    return grid


def solve(grid, rounds, part1):
    for _ in range(rounds):
        grid = sim_next_step(grid, part1)
    return list(grid.values()).count('#')


def sim_next_step(grid, part1):
    corners = [(0, 0), (0, 99), (99, 0), (99, 99)]
    new_grid = dict() 
    for pos, status in grid.items():
        neighbors = get_neigbors(pos, grid)
        if pos in corners and not part1:
            new_grid[pos] = "#"
        elif status == '#':
            new_grid[pos] = '#' if neighbors == 2 or neighbors == 3 else '.'
        else:
            new_grid[pos] = '#' if neighbors == 3 else '.'
    return new_grid


def get_neigbors(pos, grid):
    neighbors = 0
    DIRS = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    x, y = pos
    for dx ,dy in DIRS:
        if (x + dx, y+ dy) in grid:
            if grid[(x + dx, y + dy)] == '#':
                neighbors += 1
    return neighbors


if __name__ == '__main__':
    main()

