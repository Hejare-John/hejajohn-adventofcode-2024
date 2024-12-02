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

right.sort()

counted = {}
unseen = []
score = 0

for i in range(len(left)):
  l = left[i]
  if l in counted:
    score += l * counted[l]
    continue
  if l in unseen:
    continue
  j = 0
  while j < len(right):
    if l == right[j]:
      break
    j += 1
  k = j + 1
  while k < len(right):
    if l != right[k]:
      break
    k += 1
  if j >= len(right):
    unseen.append(l)
    continue
  count = k - j
  counted[l] = count
  right = right[:j] + right[k:]

  score += l * count

print("sc0re: ", score)
