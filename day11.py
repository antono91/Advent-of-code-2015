import re


def main():
    part1 = solve('hxbxwxba')
    print(part1, solve(part1))


def solve(password):
    password = next_pass(password)
    while not is_valid_pass(password):
        password = next_pass(password)
    return password


def is_valid_pass(password):
    conditions = []
    for i in range(len(password) - 2):
        c1, c2, c3 = password[i: i + 3]
        conditions.append(ord(c1) == ord(c2) - 1 == ord(c3) - 2)
    if not any(conditions):
        return False
    if any(x in password for x in 'iol'):
        return False
    if len(set(re.findall(r'([a-z])\1', password))) < 2:
        return False
    return True


def next_pass(password):
    nc = chr((ord(password[-1]) - 96) % 26 + 97)
    if nc != 'a':
        return password[:-1] + nc
    return next_pass(password[:-1]) + nc


if __name__ == '__main__':
    main()
