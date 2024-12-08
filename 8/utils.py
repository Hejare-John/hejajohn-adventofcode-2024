import math

class Mat:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def __iter__(self):
    self._iteration = 0
    return self
  
  def __next__(self):
    val = (self._iteration % self.width, math.floor(self._iteration / self.width))
    if val[1] == self.height:
      raise StopIteration
    self._iteration += 1
    return val
  
  def contains(self, pos):
    return pos[0] >= 0 and pos[0] < self.width and pos[1] >= 0 and pos[1] < self.height


def print_mat(mat):
  for y in range(len(mat)):
    row = mat[y]
    print("".join(["#" if x > 0 else "." for x in row]))