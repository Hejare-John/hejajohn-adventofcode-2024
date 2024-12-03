import re

input = open("input.txt", "r")

memory_sum = 0

for line in input.readlines():
  if line.strip() == "":
    continue
  
  matches = re.findall("mul\\(([0-9]{1,3}),([0-9]{1,3})\\)", line.strip())
  mul_sum = 0
  for m in matches:
    a = int(m[0])
    b = int(m[1])
    mul_sum += a * b
  memory_sum += mul_sum

print("sum:", memory_sum)