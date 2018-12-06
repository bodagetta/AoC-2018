filename = "sample.txt"

coors = []

def distance_to_coor(c):
    global coors

    for e in coors:
        distance = abs(c[0]-e[0]) + abs(c[1]-e[1])
        if distance > 0:
            print(distance)

with open(filename) as my_file:
        for line in my_file:
            line = line.strip()
            x_coor = int(line.split(",")[0].strip())
            y_coor = int(line.split(",")[1].strip())
            coors.append([x_coor, y_coor])

for c in coors:
    distance_to_coor(c)
    print("---")
