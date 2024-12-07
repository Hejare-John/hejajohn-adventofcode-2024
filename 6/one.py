from utils import *

input = open("input.txt", "r")

marker_map = {
  ".": 0,
  "#": 1,
  "^": 2,
}
reverse_marker_map = [".", "#", "X"]

mat = [[marker_map[x] for x in line.strip()] for line in input.readlines()]
[pos] = [(mat[y].index(2), y) for y in range(len(mat)) if 2 in mat[y]]
direction = (0, -1)
unique_positions = 1

while True:
  new_pos = (pos[0] + direction[0], pos[1] + direction[1])
  if pos_is_inside(mat, new_pos):
    if mat[new_pos[1]][new_pos[0]] == 1:
      direction = rotate_direction(direction)
    else:
      pos = new_pos
      if mat[pos[1]][pos[0]] == 0:
        mat[pos[1]][pos[0]] = 2
        unique_positions += 1
  else:
    break

print("unique positions:", unique_positions)
