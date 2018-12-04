filename = "input.txt"

fabric_map = []
fabric_size = 1000

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

def processLine(line):
    global fabric_map
    array = line.split(" ")
    id = array[0]
    array[2] = array[2].replace(':', '')
    left_edge = int(array[2].split(',')[0])
    top_edge = int(array[2].split(',')[1])

    width = int(array[3].split('x')[0])
    height = int(array[3].split('x')[1])


    for x in range(left_edge, (left_edge + width)):
        for y in range(top_edge, (top_edge+height)):
            print(x, ": ", y)
            fabric_map[x][y] += 1
            # print_map()


init_array()

# print_map()

with open(filename) as my_file:
    for line in my_file:
        processLine(line.strip())

count_overlaps()
