import math
from itertools import combinations


def main():
    with open('day24.in') as f:
        packeges = [int(n) for n in f]

    print(solve(packeges, True))
    print(solve(packeges, False))


def solve(packages, part1):
    weight = sum(packages) // 3 if part1 else sum(packages) // 4
    for i in range(10):
        if any(sum(comb) == weight for comb in combinations(packages, i)):
            group1_count = i
            break

    qe = [math.prod(group1) for group1 in combinations(packages, group1_count) if sum(group1) == weight]
    return min(qe)


if __name__ == '__main__':
    main()
