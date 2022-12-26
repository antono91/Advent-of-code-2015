def main():
    with open('day07.in') as f:
        data = [line.strip().split(' -> ') for line in f]
    print(solve(data))


def solve(data):
    wires = dict()
    for op, wire in data:
        wires[wire] = op

    part1 = evaluate_node('a', wires)
    wires['b'] = str(part1)
    results.clear()
    part2 = evaluate_node('a', wires)
    return part1, part2


results = dict()


def evaluate_node(node, wires):
    ops = {'AND': '&', 'OR': '|', 'RSHIFT': '>>', 'LSHIFT': '<<'}
    if node in results:
        return results[node]
    if node.isdigit():
        return node

    op = wires[node].split()
    if len(op) == 1:
        res = evaluate_node(op[0], wires)
    elif len(op) == 2:
        res = eval(f"~{ evaluate_node(op[1], wires) } & 0xffff")
    elif len(op) == 3:

        left, o, right = op[0], op[1], op[2]
        res = eval(
            f"{evaluate_node(left, wires)} {ops[o]} {evaluate_node(right, wires)}")
    results[node] = res
    return res


if __name__ == '__main__':
    main()
