import math

input = open("input.txt", "r")

data = [int(x) for x in input.read().strip()]
memory = [-1 for _ in range(sum(data))]
files = [x for i, x in enumerate(data) if i % 2 == 0]

# Fill memory
i = 0
for j, size in enumerate(data):
  id = int(math.floor(j / 2))
  for k in range(size):
    memory[i + k] = id if j % 2 == 0 else -1
  i += size

# Calculate memory spaces
cur_id = -1
ids = [-1 for _ in range(len(files))]
spaces = [[] for _ in range(len(memory))]
i = 0
while i < len(memory):
  if memory[i] != -1:
    if memory[i] != cur_id:
      cur_id = memory[i]
      ids[cur_id] = i
    i += 1
    continue
  j = i
  while j < len(memory) and memory[j] == -1:
    j += 1
  if j - i > 0:
    spaces[j - i].append(i)
    i = j
  else:
    i += 1

for i in range(len(spaces)):
  if len(spaces[i]) > 0:
    spaces[i].sort()

# rearrange memory
for i, size in enumerate(reversed(files)):
  id = len(files) - 1 - i
  j = ids[id]
  slot = size
  for k in range(len(spaces)):
    if k < size or len(spaces[k]) == 0:
      continue
    if len(spaces[slot]) == 0 or spaces[k][0] < spaces[slot][0]:
      slot = k
  if len(spaces[slot]) == 0:
    continue
  k = spaces[slot][0]
  if k >= j:
    continue
  spaces[slot].pop(0)
  for l in range(size):
    memory[j + l] = -1
    memory[k + l] = id
  if slot > size:
    reminder = slot - size
    l = k + size
    spaces[reminder].append(l)
    spaces[reminder].sort()

# print(memory)

checksum = 0

for i, id in enumerate(memory):
  if id == -1:
    continue
  checksum += i * id

print("checksum:", checksum)