def main():
    with open('day23.in') as f:
        programm = [line.strip() for line in f]
    print(run(programm, True))
    print(run(programm, False))


def run(programm, part1):
    pp = 0
    registers = {'a': 0 if part1 else 1, 'b': 0}
    
    while 0 <= pp < len(programm):
        inst = programm[pp]
        if inst.startswith('jio') or inst.startswith('jie'):
            jmp, reg, val = inst[:3], inst[4], int(inst[7:])
            if jmp == 'jio' and registers[reg] == 1:
                pp += val
            elif jmp == 'jie' and not registers[reg] % 2:
                pp += val
            else:
                pp += 1
        elif inst.startswith('jmp'):
            pp += int(inst[4:])
        else:
            ins, reg = inst[:3], inst[4]
            if ins == 'inc':
                registers[reg] += 1
            elif ins == 'tpl':
                registers[reg] *= 3
            elif ins == 'hlf':
                registers[reg] //= 2
            pp += 1
    return registers


if __name__ == '__main__':
    main()
 
