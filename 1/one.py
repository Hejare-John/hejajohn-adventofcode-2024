import re

input = open("input.txt", "r")

left = []
right = []

for line in input.readlines():
  if line.strip() == "":
    continue
  [l, r] = re.split("\s+", line.strip())
  left.append(int(l))
  right.append(int(r))

left.sort()
right.sort()

diffs = []

for i in range(len(left)):
  diffs.append(abs(left[i] - right[i]))

diff_sum = sum(diffs)

print("sum: ", diff_sum)
