import re
import report

input = open("input.txt", "r")

safe_reports = 0

for line in input.readlines():
  if line.strip() == "":
    continue
  
  numbersStr = re.split("\\s+", line.strip())
  numbers = [int(x) for x in numbersStr]

  if report.check_report_dampened(numbers) or report.check_report_dampened(numbers[1:], True):
    safe_reports += 1

print("safe reports:", safe_reports)