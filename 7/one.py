from utils import *

input = open("input.txt", "r")

result_sum = 0

for line in input.readlines():
  [result_str, equation_str] = line.strip().split(": ")
  result = int(result_str)
  equation = [int(x) for x in equation_str.split(" ")]
  if find_solution(equation, result):
    result_sum += result

print("result sum:", result_sum)