import itertools


# read the input with the input_reader and call the graph_builder
def main():
    # data = (all_coordinates, all_combinations_of_disks, max_y_value)
    data = input_reader()
    graph_builder(data[0], data[1], data[2])


# given input, find n, m, w, make a list of all coordinates and all combinations of disks
# return list of coordinates, list of disk combinations and W (max y value)
def input_reader():
    values = input()
    n = int(values.split(' ')[0])
    m = int(values.split(' ')[1])
    w = int(values.split(' ')[2])
    coordinates = []
    disks = []
    # read all lines with coordinates
    for i in range(0, n):
        next_line = input()
        coordinate = (int(next_line.split()[0]), int(next_line.split()[1]))
        coordinates.append(coordinate)
    # read all lines with disk radius and cost
    for i in range(0, m):
        next_line = input()
        disk_cost = (int(next_line.split()[0]), int(next_line.split()[1]))
        disks.append(disk_cost)
    # make combinations of every disk radius and cost and sort them ascending on cost
    disk_combinations = list(
        tuple((x[0] + y[0], x[1] + y[1]) for x, y in itertools.combinations_with_replacement(disks, 2)))
    disk_combinations.sort(key=lambda x: x[1])

    return coordinates, disk_combinations, w


# take out coordinate one by one, and call connect_edges to try to connect the coordinate to
# all other coordinates, for the lowest possible cost
def graph_builder(coordinates, disks, w):
    graph = []
    for j in range(0, len(coordinates)):
        current = coordinates[0]
        coordinates.remove(current)
        connect_edges(current, coordinates, graph, disks, w)
    print(graph)


# given a current node, loop through all disks to try to connect it to the start(y=0) and end(y=w)
# then loop through list of coordinates and list of disks and connect current to every
# possible coordinate for the lowest possible cost
def connect_edges(current, coordinates, graph, disks, W):
    for smallest_disk in disks:
        if current[1] <= smallest_disk[0]:
            graph.append(("start", current, smallest_disk[1]))
            break
        if abs(current[1] - W) <= smallest_disk[0]:
            graph.append((current, "end", smallest_disk[1]))
            break
    for coordinate in coordinates:
        for smallest_disk in disks:
            if abs(current[0] - coordinate[0]) <= (smallest_disk[0]) and abs(current[1] - coordinate[1]) <= (
                    smallest_disk[0]):
                graph.append((current, coordinate, smallest_disk[1]))
                break


main()
