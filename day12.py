import re
import json


def main():
    with open('day12.in') as f:
        line = f.read().strip()
    print(solve(line))


def solve(s):
    objects = json.loads(re.findall(r"\{.+\}", s)[0])
    print(len(objects))
    # return sum(map(int, re.findall(r"-?\d+", s)))


if __name__ == '__main__':
    main()
