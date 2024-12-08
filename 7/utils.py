class Permutator:
  def __init__(self, slots, size):
    self.slots = slots
    self.size = size
  
  def __iter__(self):
    self._iteration = 0
    self.permutation = [0 for _ in range(self.slots)]
    return self

  def __next__(self):
    for i in range(self.slots):
      self.permutation[i] += 1
      if self.permutation[i] < self.size:
        break
      self.permutation[i] = 0
    if self._iteration > 0 and sum(self.permutation) == 0:
      raise StopIteration
    self._iteration += 1
    return self.permutation


def calculate_equation_plus_times(equation, permutation):
  res = equation[0]
  for i, p in enumerate(permutation):
    if p == 0:
      res += equation[i + 1]
    else:
      res *= equation[i + 1]
  return res


def find_solution(equation, result):
  for permutation in iter(Permutator(len(equation) - 1, 2)):
    if result == calculate_equation_plus_times(equation, permutation):
      return True
  return False
