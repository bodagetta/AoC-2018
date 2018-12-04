filename = "sample.txt"

fabric_map = []
fabric_size = 1000
claims_info = []

non_overlapping = []

def init_array():
    global fabric_map

    line = []

    for i in range(0, fabric_size):
        line.append(0)

    for i in range(0, fabric_size):
        fabric_map.append(line.copy())

def print_map():
    global  fabric_map

    for i, row in enumerate(fabric_map):
        print(row)

    print("-----")

def count_overlaps():
    global fabric_map

    count = 0

    for row in fabric_map:
        for e in row:
            if e > 1:
                count = count + 1

    print(count)

def processData(id, left_edge, top_edge, width, height, run_count):
    global fabric_map

    could_be_nonoverlapping = True

    for x in range(left_edge, (left_edge + width)):
        for y in range(top_edge, (top_edge+height)):
            print(x, ": ", y)
            fabric_map[x][y] += 1
            if fabric_map[x][y] > 2:
                could_be_nonoverlapping = False
            # print_map()

    if could_be_nonoverlapping:
        if run_count > 1:
            non_overlapping.append(id)



def processLine(line):
    global fabric_map
    global claims_info
    global non_overlapping

    array = line.split(" ")
    id = array[0]
    array[2] = array[2].replace(':', '')
    left_edge = int(array[2].split(',')[0])
    top_edge = int(array[2].split(',')[1])

    width = int(array[3].split('x')[0])
    height = int(array[3].split('x')[1])

    claims_info.append([id, left_edge, top_edge, width, height])

init_array()

# print_map()

with open(filename) as my_file:
    for line in my_file:
        processLine(line.strip())

for l in claims_info:
    processData(l[0], l[1], l[2], l[3], l[4], 1)

count_overlaps()

for l in claims_info:
    processData(l[0], l[1], l[2], l[3], l[4], 2)


print("Non Overlapping Claims: ", non_overlapping)
