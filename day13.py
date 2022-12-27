from itertools import permutations


def main():
    happiness = dict()
    names = set()
    with open('day13.in') as f:
        for line in f.readlines():
            line = line.split()
            name = line[0]
            val = int(line[3]) if line[2] == 'gain' else -int(line[3])
            neighbor = line[-1][:-1]
            names.add(name)
            happiness[(name, neighbor)] = val

    print(solve(happiness, names))
    for n in names:
        happiness[('me', n)] = 0
        happiness[(n, 'me')] = 0
    names.add('me')
    print(solve(happiness, names))


def solve(happiness, names):
    return max(calc_happiness(table, happiness) for table in permutations(names))


def calc_happiness(table, happiness):
    s = 0
    for i, name in enumerate(table):
        if i == 0:
            n1, n2, n3 = table[-1], table[0], table[1]
        elif i == len(table) - 1:
            n1, n2, n3 = table[i - 1], table[-1], table[0]
        else:
            n1, n2, n3 = table[i - 1:i + 2]
        s += happiness[(n2, n1)] + happiness[(n2, n3)]
    return s


if __name__ == '__main__':
    main()
