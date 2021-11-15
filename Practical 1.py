
all_paths = []


def main():
    # data = (all_coordinates, all_combinations_of_disks, max_y_value)
    data = input_reader()
    # place_largest_disk(data[0], data[1], data[2])


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
    disks.sort(key=lambda x: x[1], reverse=True)
    return coordinates, disks, w


def place_largest_disk(current, coordinates, disks, w, graph):
    if current[1] <= disks[0][0]:
        graph.append(((current[0], 0), current, 0, disks[0][0], disks[0][1]))
    if abs(current[1] - w) <= disks[0][0]:
        graph.append((current, (current[0], w), disks[0][0], 0, disks[0][1]))
    for coordinate in coordinates:
        if abs(current[0] - coordinate[0]) <= 2 * disks[0][0] and abs(current[1] - coordinate[1]) <= 2 * disks[0][0]:
            graph.append((current, coordinate, disks[0][0], disks[0][0], 2 * disks[0][1]))


def find_paths(graph, current, path, w):
    path.append(current)
    if current[1][1] == w:
        all_paths.append(path)
    for node in graph:
        if node not in path and current[1] == node[0]:
            find_paths(graph, node, path, w)


def complete_path(path):
    complete_path = True
    for i in range(0, len(path)-1):
        if abs(path[i][0][0] - path[i+1][0][0]) > (path[i][2] + path[i+1][2]) and abs(path[i][0][1] - path[i+1][0][1]) > (path[i][2] + path[i+1][2]):
            complete_path = False
    return complete_path


def graph_builder(coordinates, disks, w):
    graph = []
    for j in range(0, len(coordinates)):
        current = coordinates[0]
        coordinates.remove(current)
        place_largest_disk(current, coordinates, disks, w, graph)
    print(graph)
    for node in graph:
        if node[0][1] == 0:
            path = find_paths(graph, node, [], w)
            all_paths.append(path)
    print(all_paths[0])
    print(all_paths[1])
    print(all_paths[2])
    print("a")
    print(len(all_paths))


    


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
