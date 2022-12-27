import re


def main():
    with open('day15.in') as f:
        lines = [line.strip() for line in f]
    print(solve(lines))


def solve(lines):
    ingredients = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]
    part1 = part2 = 0
    for p1 in range(101):
        for p2 in range(101 - p1):
            for p3 in range(101 - p1 - p2):
                p4 = 100 - p1 - p2 - p3
                score = 1
                calories = 0
                for i in range(4):
                    s = p1 * ingredients[0][i] + p2 * ingredients[1][i] + p3 * ingredients[2][i] + p4 * ingredients[3][
                        i]
                    calories = p1 * ingredients[0][4] + p2 * ingredients[1][4] + p3 * ingredients[2][4] + p4 * \
                               ingredients[3][4]
                    score *= s if s > 0 else 0
                if calories == 500:
                    part2 = max(part2, score)
                part1 = max(part1, score)

    return part1, part2


if __name__ == '__main__':
    main()
