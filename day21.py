def main():
    print(solve(103, 9, 2))


def solve(b_hp, b_dmg, b_armor):
    weapons = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]
    armor = [(13, 1), (31, 2), (53, 3), (75, 4),(102,5)]
    ring_dmg = [(0, 0), (25, 1), (50, 2), (100, 3)]
    ring_armor = [(0, 0), (20, 1), (40, 2), (80, 3)]
    min_costs, max_costs = 10000, 0
    for c1, dmg1 in weapons:
        for c2, a1 in armor:
            for c3, dmg2 in ring_dmg:
                for c4, a2 in ring_armor:
                    costs = c1 + c2 + c3 + c4
                    dmg = dmg1 + dmg2
                    ar = a1 + a2
                    if fight(100, dmg, ar, b_hp, b_dmg, b_armor):
                        min_costs = min(costs, min_costs)
                    else:
                        max_costs = max(costs, max_costs)
    return min_costs, max_costs


def fight(p_hp, p_dmg, p_armor, b_hp, b_dmg, b_armor):
    rounds = 0
    while True:
        rounds += 1
        b_hp -= p_dmg - b_armor if b_armor < p_dmg else 1
        if b_hp <= 0:
            return True
        p_hp -= b_dmg - p_armor if p_armor < b_dmg else 1
        if p_hp <= 0:
            return False


if __name__ == '__main__':
    main()

