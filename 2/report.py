def check_report(numbers):
  i = 0
  slope = 0
  while i < len(numbers) - 1:
    diff = numbers[i + 1] - numbers[i]
    if slope != 0 and slope != get_sign(diff):
      return False
    else:
      slope = get_sign(diff)
    if not (1 <= abs(diff) <= 3):
      return False
    i += 1
  return True


def check_report_dampened(numbers, dampened = False):
  i = 0
  slope = 0
  while i < len(numbers) - 1:
    [ok, slope] = check_pair(numbers[i], numbers[i + 1], slope)
    if ok:
      i += 1
      continue
    # check bad level
    if dampened:
      return False
    if i >= len(numbers) - 2:
      return False
    [ok, slope] = check_pair(numbers[i], numbers[i + 2], slope)
    if ok:
      dampened = True
      i += 2
      continue
    return False
  return True


def check_report_recursive(numbers):
  if check_report(numbers):
    return True
  for i in range(len(numbers)):
    sub_numbers = numbers[:i] + numbers[i + 1:]
    if check_report(sub_numbers):
      return True
  return False

def check_pair(a, b, slope):
  diff = b - a
  diff_slope = get_sign(diff)
  if slope != 0 and slope != diff_slope:
    return [False, slope]
  if not (1 <= abs(diff) <= 3):
    return [False, slope]
  return [True, diff_slope]


def get_sign(n):
  return 1 if n >= 0 else -1