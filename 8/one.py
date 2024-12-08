from utils import *

input = open("input.txt", "r")

map = [[x for x in line.strip()] for line in input.readlines()]

width = len(map[0])
height = len(map)
mat = Mat(width, height)

ant_mat = [[0 for _ in range(width)] for _ in range(height)]
ant_pos = {}

for (x, y) in iter(mat):
  marker = map[y][x]
  if marker == ".":
    continue
  if not marker in ant_pos:
    ant_pos[marker] = []
  ant_pos[marker].append((x, y))

for marker in ant_pos:
  positions = ant_pos[marker]
  for i, a in enumerate(positions):
    for j in range(i + 1, len(positions)):
      b = positions[j]
      dx = a[0] - b[0]
      dy = a[1] - b[1]
      A = (a[0] + dx, a[1] + dy)
      B = (b[0] - dx, b[1] - dy)
      if mat.contains(A):
        ant_mat[A[1]][A[0]] += 1
      if mat.contains(B):
        ant_mat[B[1]][B[0]] += 1

unique_positions = 0

for (x, y) in iter(mat):
  if ant_mat[y][x] > 0:
    unique_positions += 1

print("unique positions:", unique_positions)