def pos_is_inside(mat, pos):
  return pos[0] >= 0 and pos[0] < len(mat[0]) and pos[1] >= 0 and pos[1] < len(mat)

def rotate_direction(direction):
  if direction[0] < 0:
    return (0, -1)
  elif direction[0] > 0:
    return (0, 1)
  elif direction[1] < 0:
    return (1, 0)
  return (-1, 0)

def direction_to_bit(direction):
  if direction[0] < 0:
    return 2
  elif direction[0] > 0:
    return 4
  elif direction[1] < 0:
    return 8
  return 16

def print_mat(mat, obstacle = None):
  reverse_marker_map = {
    0: ".",
    1: "#",
    2: "←",
    4: "→",
    8: "↑",
    16: "↓",
  }
  for y in range(len(mat)):
    row = mat[y]
    print("".join(["O" if obstacle and x == obstacle[0] and y == obstacle[1] else (reverse_marker_map[x] if x in reverse_marker_map else "+") for x in row]))

def loop_detector(mat, obstacle, pos, direction):
  mat = [row.copy() for row in mat]
  mat[obstacle[1]][obstacle[0]] = 1
  pos = (pos[0], pos[1])
  direction = (direction[0], direction[1])

  while True:
    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if pos_is_inside(mat, new_pos):
      if mat[new_pos[1]][new_pos[0]] == 1:
        direction = rotate_direction(direction)
      else:
        pos = new_pos
      bit = direction_to_bit(direction)
      if mat[pos[1]][pos[0]] & bit != 0:
        # print("pos:", pos)
        # print(mat[pos[1]][pos[0]], ",", bit)
        # print_mat(mat, obstacle)
        return True
      mat[pos[1]][pos[0]] |= bit
    else:
      return False