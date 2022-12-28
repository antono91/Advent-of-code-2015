from itertools import combinations


def main():
    with open('day17.in') as f:
        containers = [int(line) for line in f]
    print(solve(containers))


def solve(containers):
    part1 = part2 = 0
    for i in range(len(containers)):
        if not any(sum(comb) == 150 for comb in combinations(containers, i)):
            continue
        for comb in combinations(containers, i):
            if sum(comb) == 150:
                part1 += 1
                if i == 4:
                    part2 += 1

    return part1, part2


if __name__ == '__main__':
    main()
