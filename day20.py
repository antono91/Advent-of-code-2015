import numpy as np

def main():
    print(solve(34000000, False))

def solve(num, part1):
    for house in range(500000, 10000000):
        divs = np.array(divisors(house))
        multi = 10 if part1 else 11
        presents = sum(divs * multi) 
        print(house, presents)
        if presents >= num:
            return house


def divisors(n):
    result = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    return list(result)


if __name__ =='__main__':
    main()
