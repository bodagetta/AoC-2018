filename = "input.txt"

two_count = 0
three_count = 0

def processCounts(line):
    global two_count
    global three_count

    count_dict = {}
    for a in line:
        if a in count_dict:
            count_dict[a] += 1
        else:
            count_dict[a] = 1

    contains_two = False
    contains_three = False

    for key in count_dict:
        if count_dict[key] == 2:
            contains_two = True
        if count_dict[key] == 3:
            contains_three = True

    if contains_two:
        two_count += 1

    if contains_three:
        three_count += 1





with open(filename) as my_file:
    for line in my_file:
        processCounts(line.strip())

print("Two Count: ", two_count)
print("Three Count: ", three_count)
print("Checksum: ", two_count * three_count)
