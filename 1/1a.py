filename = "input.txt"

frequency = 0

with open(filename) as my_file:
    for line in my_file:
        frequency += int(line)

print(frequency)
