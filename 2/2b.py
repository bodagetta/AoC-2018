filename = "input.txt"

data_array = []
similar_array = []

def process_line(line):
    global data_array
    global compare_line

    line_length = len(line)

    for compare_line in data_array:
        difference_count = 0
        for i, c in enumerate(compare_line):
            if line[i] != compare_line[i]:
                difference_count += 1

        if difference_count == 1:
            if line not in similar_array:
                similar_array.append(line)
            if compare_line not in similar_array:
                similar_array.append(compare_line)

with open(filename) as my_file:
    for line in my_file:
        data_array.append(line.strip())

for line in data_array:
    process_line(line)

output_word = ""

first_box = similar_array[0]
second_box = similar_array[1]

for i, c in enumerate(first_box):
    if first_box[i] == second_box[i]:
        output_word += first_box[i]

print(output_word)
