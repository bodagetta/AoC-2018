filename = "input.txt"

data = ""

def process_suit():
    global data
    number_of_changes = 0
    new_data = ""
    skip_next = False
    for index, e in enumerate(data):
        if index < (len(data) - 2):
            if e.isupper() and not data[index+1].isupper():
                if e == data[index+1].upper():
                    data = data[:index] + data[index+2:]
                    return 1
            elif not e.isupper() and data[index+1].isupper():
                if e.upper() == data[index+1]:
                    data = data[:index] + data[index+2:]
                    return 1

    return 0

with open(filename) as my_file:
    for line in my_file:
        data = line.strip()


number_of_changes = 99

while number_of_changes > 0:
    number_of_changes = process_suit()
    print(len(data))



print(len(data))
