import math

class Mat:
  def __init__(self, width, height, default = None):
    self.width = width
    self.height = height
    self.map = [[default for _ in range(width)] for _ in range(height)]
  
  def __iter__(self):
    self._iteration = 0
    return self
  
  def __next__(self):
    val = (self._iteration % self.width, math.floor(self._iteration / self.width))
    if val[1] == self.height:
      raise StopIteration
    self._iteration += 1
    return val
  
  @staticmethod
  def from_input(filename, callback = None):
    input = open(filename, "r")

    map = [[callback(x) if callback else x for x in line.strip()] for line in input.readlines()]
    mat = Mat(len(map[0]), len(map))
    mat.map = map

    return mat

  def get(self, x, y):
    if self.contains(x, y):
      return self.map[y][x]
    return None

  def contains(self, pos):
    return pos[0] >= 0 and pos[0] < self.width and pos[1] >= 0 and pos[1] < self.height
