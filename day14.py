import re


def main():
    with open('day14.in') as f:
        lines = [line.strip() for line in f]

    print(solve(lines, 2503))


def solve(lines, t):
    reindeers = []
    for line in lines:
        reindeers.append([0, 0, False, 0] + list(map(int, re.findall(r"\d+", line))))

    results = calc_dist_points(reindeers, 2503)
    part1 = max(r[0] for r in results)
    part2 = max(r[1] for r in results)
    return part1, part2


def calc_dist_points(reindeers, e):
    t = 1
    while t <= e:
        # calc dist
        for _ in range(len(reindeers)):
            dist, points, is_resting, resting_end, speed, duration, rest = reindeers.pop(0)
            if not is_resting:
                dist += speed
            if resting_end + duration == t:
                is_resting = True
                resting_end = t + rest
            if is_resting and t == resting_end:
                is_resting = False
            reindeers.append([dist, points, is_resting, resting_end, speed, duration, rest])
        t += 1

        # calc points
        max_dist = max(reindeer[0] for reindeer in reindeers)
        for reindeer in reindeers:
            if reindeer[0] == max_dist:
                reindeer[1] += 1

    return reindeers


if __name__ == '__main__':
    main()
