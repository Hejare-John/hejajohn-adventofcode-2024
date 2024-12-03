import re

def find_mul(str):
  match = re.search("mul\\(([0-9]{1,3}),([0-9]{1,3})\\)", str)
  if not match:
    return [None, None]
  a = int(match[1])
  b = int(match[2])
  mul = a * b
  return [match.span(), mul]


def find_enable(str):
  match = re.search("do\\(\\)", str)
  if not match:
    return None
  return match.span()


def find_disable(str):
  match = re.search("don't\\(\\)", str)
  if not match:
    return None
  return match.span()


input = open("input.txt", "r")

memory_sum = 0
enabled = True

for line in input.readlines():
  if line.strip() == "":
    continue
  
  mul_sum = 0

  while len(line) > 0:
    disable_index = find_disable(line)
    if enabled:
      [mul_index, mul] = find_mul(line)
      if disable_index and (not mul_index or disable_index[0] < mul_index[0]):
        enabled = False
        line = line[disable_index[1]:]
        continue
      if mul_index:
        mul_sum += mul
        line = line[mul_index[1]:]
      else:
        break
    else:
      enable_index = find_enable(line)
      if enable_index:
        enabled = True
        line = line[enable_index[1]:]
        continue
      break
  
  memory_sum += mul_sum

print("sum:", memory_sum)
