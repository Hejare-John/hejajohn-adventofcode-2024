import re
input = open("example.txt", "r")

input_lines = input.readlines()
input_divider_index = input_lines.index("\n")

page_order = []
updates = []
max_page_number = 0

for line in input_lines[input_divider_index+1:]:
  update = [int(x) for x in line.strip().split(",")]
  max_page_number = max(max_page_number, max(update))
  updates.append(update)

page_order = [[] for _ in range(max_page_number + 1)]

for line in input_lines[:input_divider_index]:
  match = re.match("([0-9]+)\\|([0-9]+)", line)
  a = int(match[1])
  b = int(match[2])
  page_order[a].append(b)

print(page_order)
