from itertools import permutations


def main():
    places = set()
    distances = dict()
    with open('day09.in') as f:
        for line in f:
            p1, _, p2, _, dist = line.strip().split()
            places.add(p1)
            places.add(p2)
            distances[(p1, p2)] = int(dist)
            distances[(p2, p1)] = int(dist)
    print(solve(places, distances))


def solve(places, distances):
    shortest = int(1e6)
    longest = 0
    for path in permutations(places):
        dist = 0
        d = sum(distances[(p1, p2)]
                for p1, p2 in zip(list(path), list(path)[1:]))
        shortest = min(d, shortest)
        longest = max(d, longest)
    return shortest, longest


if __name__ == '__main__':
    main()
