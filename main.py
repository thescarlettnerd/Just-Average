data = input("Enter your data without commas, separated by a space.\n").split()
for n in range(0, len(data)):
  data[n] = int(data[n])

data_points = 0
for numbers in data:
  data_points += 1

total_sum = 0
for numbers in data:
  total_sum += int(numbers)

print("The average is: " + str(int(total_sum) / int(data_points)))