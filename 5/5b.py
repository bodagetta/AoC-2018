import string
import cProfile as profile

filename = "input.txt"

original_data = ""
data = ""

def process_suit():
    global data
    number_of_changes = 0
    new_data = ""
    skip_next = False
    for index, e in enumerate(data):
        if index < (len(data) - 1):
            if e.isupper() and not data[index+1].isupper():
                if e == data[index+1].upper():
                    data = data[:index] + data[index+2:]
                    return 1
            elif not e.isupper() and data[index+1].isupper():
                if e.upper() == data[index+1]:
                    data = data[:index] + data[index+2:]
                    return 1

    return 0


def main():
    global data
    global original_data

    with open(filename) as my_file:
        for line in my_file:
            original_data = line.strip()

    len_array = []

    for index, e in enumerate(string.ascii_lowercase):
        if (e in original_data) or (e.upper() in original_data):
            new_data = original_data.replace(e, "")
            new_data = new_data.replace(e.upper(), "")
            data = new_data
            number_of_changes = 99
            while number_of_changes > 0:
                number_of_changes = process_suit()

            print(e, ": ", len(data))
            len_array.append(len(data))
        else:
            print("Skipping ", e)


    print("Smallest String: ", min(len_array))


profile.run('main()')
