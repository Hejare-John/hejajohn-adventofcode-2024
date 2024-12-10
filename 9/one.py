import math

input = open("input.txt", "r")

data = [int(x) for x in input.read().strip()]
memory = [-1 for _ in range(sum(data))]

i = 0
for j, size in enumerate(data):
  id = int(math.floor(j / 2))
  for k in range(size):
    memory[i + k] = id if j % 2 == 0 else -1
  i += size

j = len(memory) - 1
for i in range(len(memory)):
  if memory[i] != -1:
    continue
  while memory[j] == -1:
    j -= 1
  if i >= j:
    break
  memory[i], memory[j] = memory[j], -1

checksum = 0

for i, id in enumerate(memory):
  if id == -1:
    break
  checksum += i * id

print("checksum:", checksum)