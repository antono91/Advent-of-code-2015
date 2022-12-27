import re

with open('input.txt', 'r') as f:
  data = [line.strip() for line in f]


def solve(data):
  mem = chars =  encoded = 0

  for s in data:
    res = re.sub(r'\\"', 'y', s)
    res = re.sub(r'\\\\', 'z', res)
    res = re.sub(r'\\x[0-9a-fA-F]{2}', 'x', res)

    mem += len(s)
    chars += len(res[1:-1])

    res2 = re.sub(r"\\", "xx", s)
    res2 = '"' + re.sub(r"\"", '\\"', res2) + '"'
    
    encoded += len(res2)

  return mem - chars, encoded - mem


print(solve(data))