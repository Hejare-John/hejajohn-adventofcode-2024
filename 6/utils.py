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