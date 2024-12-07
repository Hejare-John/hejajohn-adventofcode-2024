from utils import *

input = open("input.txt", "r")

marker_map = {
  ".": 0,
  "#": 1,
  "^": 2,
}

mat = [[marker_map[x] for x in line.strip()] for line in input.readlines()]
[pos] = [(mat[y].index(2), y) for y in range(len(mat)) if 2 in mat[y]]
mat[pos[1]][pos[0]] = 0
direction = (0, -1)
obstacle_positions = 0

for x in range(len(mat[0])):
  for y in range(len(mat)):
    if mat[y][x] == 1 or (x == pos[0] and y == pos[1]):
      continue
    if loop_detector(mat, (x, y), pos, direction):
      obstacle_positions += 1

print("unique positions:", obstacle_positions)
