def main():
    print(solve('1113122113', 40))
    print(solve('1113122113', 50))


def solve(num, rounds):
    for _ in range(rounds):
        num = look_and_say(num)
    return len(num)


def look_and_say(num):
    parts = []
    last_i = 0
    ans = ""
    for i, d in enumerate(num):
        if i > 0:
            if d != num[i - 1]:
                parts.append(num[last_i:i])
                last_i = i
    parts.append(num[last_i:])

    for part in parts:
        ans += str(len(part)) + part[0]
    return ans


if __name__ == '__main__':
    main()
