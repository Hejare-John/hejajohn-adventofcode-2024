input = open("input.txt", "r")

# X M A S
# 1 2 4 8

mat = []

letter_map = {
  "X": 1,
  "M": 2,
  "A": 4,
  "S": 8,
}
mas_template = letter_map['M'] + letter_map['A'] + letter_map['S']
xplore_one = [(-1, -1), (1, 1)]
xplore_two = [(1, -1), (-1, 1)]

def xplore(pos, dir):
  x = pos[0] + dir[0]
  y = pos[1] + dir[1]
  if (not (0 <= y < len(mat))) or (not (0 <= x < len(mat[0]))):
    return 0
  return mat[y][x]

for line in input.readlines():
  mat.append([letter_map[x] for x in line.strip()])

x_mas_count = 0

for y in range(len(mat)):
  for x in range(len(mat[0])):
    if mat[y][x] != letter_map['A']:
      continue
    val1 = letter_map['A'] + xplore((x, y), xplore_one[0]) + xplore((x, y), xplore_one[1])
    val2 = letter_map['A'] + xplore((x, y), xplore_two[0]) + xplore((x, y), xplore_two[1])
    if val1 == val2 == mas_template:
      x_mas_count += 1

print("x-mas count:", x_mas_count)