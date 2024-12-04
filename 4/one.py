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
xmas_template = sum([letter_map[x] for x in letter_map.keys()])
xplore_directions = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

def xplore(pos, dir, depth = 0):
  if depth > 3:
    return 0
  if (not (0 <= pos[1] < len(mat))) or (not (0 <= pos[0] < len(mat[0]))):
    return 0
  val = mat[pos[1]][pos[0]] & 2**depth
  return val + xplore((pos[0] + dir[0], pos[1] + dir[1]), dir, depth + 1)

for line in input.readlines():
  mat.append([letter_map[x] for x in line.strip()])

xmas_count = 0

for y in range(len(mat)):
  for x in range(len(mat[0])):
    for dir in xplore_directions:
      val = xplore((x, y), dir)
      if val == xmas_template:
        xmas_count += 1

print("xmas count:", xmas_count)