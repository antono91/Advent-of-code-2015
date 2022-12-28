from collections import defaultdict, deque
import re


def main():
    replacements = defaultdict(list)
    with open('day19.in') as f:
        lines, medicine   = f.read().split('\n\n')
        medicine = medicine.strip()
        for line in lines.split('\n'):
            f, t = line.split(' => ')
            replacements[f].append(t)

    print(solve(medicine, replacements))


def replace(medicine, replacements):
    molecules = set()
    for to_replace in replacements:
        if to_replace not in medicine:
            continue
        for replacement in replacements[to_replace]:
            for match in re.finditer(to_replace, medicine):
                start, end = match.span()
                molecules.add(medicine[:start] + replacement + medicine[end:])
    return molecules


def comprimise(medicine, replacements):
    steps = 0
    while medicine != 'e':
        for mol in replacements:
            for s in mol:
                if s in medicine:
                    medicine.replace(s, mol)
                    steps += 1

def solve(medicine, replacements):
    part1 = len(replace(medicine, replacements))
    print(replacements)
    for x in replacements:
        replacements[x] = sorted(replacements[x], key=lambda i: -len(i))
    print(replacements)
    print(comprimise(medicine, replacements)) 
    

    return part1, part2


if __name__ == '__main__':
    main()

