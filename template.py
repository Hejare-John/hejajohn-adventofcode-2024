input = open("example.txt", "r")

for line in input.readlines():
  if line.strip() == "":
    continue
  pass
