import string

filename = "sample.txt"

coors = []
max_size = 20

def build_array():
    global coors
    for j in range(0,max_size):
        row = []
        for i in range(0,max_size):
            row.append('.')
        coors.append(row)

def print_array():
    global coors
    for row in coors:
        print(''.join(row))

def add_coor(x,y, letter):
     global coors
     coors[x][y] = letter

def assign_owners():
    


build_array()


with open(filename) as my_file:
    file_index = 0
    for line in my_file:
        line = line.strip()
        x_coor = int(line.split(",")[0].strip())
        y_coor = int(line.split(",")[1].strip())
        add_coor(x_coor, y_coor, string.ascii_uppercase[file_index])
        file_index += 1

print_array()
