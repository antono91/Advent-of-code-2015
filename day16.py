import re


def main():
    aunts = list()
    with open('day16.in') as f:
        lines = [line.strip() for line in f]
    for i, line in enumerate(lines):
        aunt = dict()
        for item in re.findall(r"\w+: \d+", line):
            t, v = item.split(': ')
            aunt[t] = int(v)
        aunts.append(aunt)

    ticker_tape1 = {
        "children": lambda x: x == 3,
        "cats": lambda x: x == 7,
        "samoyeds": lambda x: x == 2,
        "pomeranians": lambda x: x == 3,
        "akitas": lambda x: x == 0,
        "vizslas": lambda x: x == 0,
        "goldfish": lambda x: x == 5,
        "trees": lambda x: x == 3,
        "cars": lambda x: x == 2,
        "perfumes": lambda x: x == 1
    }
    ticker_tape2 = {
        "children": lambda x: x == 3,
        "cats": lambda x: x > 7,
        "samoyeds": lambda x: x == 2,
        "pomeranians": lambda x: x < 3,
        "akitas": lambda x: x == 0,
        "vizslas": lambda x: x == 0,
        "goldfish": lambda x: x < 5,
        "trees": lambda x: x > 3,
        "cars": lambda x: x == 2,
        "perfumes": lambda x: x == 1
    }

    print(solve(aunts, ticker_tape1))
    print(solve(aunts, ticker_tape2))


def solve(aunts, ticker_tape):
    for i, aunt in enumerate(aunts, start=1):
        for item, amount in aunt.items():
            if not ticker_tape[item](amount):
                break
        else:
            return i


if __name__ == '__main__':
    main()

