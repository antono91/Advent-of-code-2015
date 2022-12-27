with open('input.txt', 'r') as f:
  data = f.read().strip()

def solve(data):
  DIR = {'^': (0, 1), 'v': (0, -1) ,'<': (-1, 0), '>': (1, 0)}
  santa = (0, 0)
  robo = (0, 0)
  visited = {santa}
  visited2 = {santa, robo}

  for move in data:
    santa = (santa[0] + DIR[move][0], santa[1] + DIR[move][1])
    visited.add(santa)

  # Part 2
  santa = (0, 0)
  for i, move in enumerate(data):
    if not i % 2:
      santa = (santa[0] + DIR[move][0], santa[1] + DIR[move][1])
      visited2.add(santa)
    else:
      robo = (robo[0] + DIR[move][0], robo[1] + DIR[move][1])
      visited2.add(robo) 
      
  
  return len(visited), len(visited2)
  

print(solve(data))