import itertools


def main():
    # data = (all_coordinates, all_combinations_of_disks, max_y_value)
    data = input_reader()
    graph_builder(data[0], data[1], data[2])


def input_reader():
    values = input()
    n = int(values.split(' ')[0])
    m = int(values.split(' ')[1])
    w = int(values.split(' ')[2])
    coordinates = []
    disks = []
    for i in range(0, n):
        next_line = input()
        coordinate = (int(next_line.split()[0]), int(next_line.split()[1]))
        coordinates.append(coordinate)
    for i in range(0, m):
        next_line = input()
        disk_cost = (int(next_line.split()[0]), int(next_line.split()[1]))
        disks.append(disk_cost)
    disk_combinations = list(
        tuple((x[0] + y[0], x[1] + y[1]) for x, y in itertools.combinations_with_replacement(disks, 2)))
    disk_combinations.sort(key=lambda x: x[1])
    return coordinates, disk_combinations, w


def graph_builder(coordinates, disks, W):
    graph = []
    for j in range(0, len(coordinates)):
        current = coordinates[0]
        coordinates.remove(current)
        build_graph(current, coordinates, graph, disks, W)
    print(graph)


def build_graph(current, coordinates, graph, disks, W):
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
