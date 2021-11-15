import math


def input_reader():
    values = input()
    n = int(values.split(' ')[0])
    m = int(values.split(' ')[1])
    w = int(values.split(' ')[2])
    coordinates = []
    disks = []
    adjacency_matrix = []
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
    disks.sort(key=lambda x: x[0], reverse=True)
    start_node = [0]
    for i in range(0, len(coordinates)):
        if coordinates[i][1] <= disks[0][0]:
            start_node.append(coordinates[i][1])
        else:
            start_node.append(0)
        edges = [0]
        for j in range(0, len(coordinates)):
            if abs(coordinates[i][0] - coordinates[j][0]) <= 2 * disks[0][0] and abs(
                    coordinates[i][1] - coordinates[j][1]) <= 2 * disks[0][0] and not i == j:
                delta_x = abs(coordinates[i][0] - coordinates[j][0])
                delta_y = abs(coordinates[i][1] - coordinates[j][1])
                edges.append(math.ceil(math.sqrt(delta_x * delta_x + delta_y * delta_y)))
            else:
                edges.append(0)
        if abs(coordinates[i][1] - w) <= disks[0][0]:
            edges.append(abs(coordinates[i][1] - w))
        else:
            edges.append(0)
        adjacency_matrix.append(edges)
    start_node.append(0)
    adjacency_matrix.insert(0, start_node)

    # for j in range(0, len(coordinates)):
    #     current = coordinates[0]
    #     coordinates.remove(current)

    return adjacency_matrix, disks


def find_all_paths(adj, u, d, visited, path, all_paths):
    visited[u] = True
    path.append(u)
    if u == d:
        if path not in all_paths:
            all_paths.append(path)
            print(len(all_paths))
    else:
        for i in range(0, len(adj[u])):
            if not visited[i] and adj[u][i] > 0:
                find_all_paths(adj, i, d, visited, path, all_paths)

    path.pop()
    visited[u] = False


def find_all_paths2(adj, u, d, visited, path, all_paths, disks, total_cost):
    visited[u] = True
    path.append(u)
    if u == d:
        all_paths.append(total_cost)
    else:
        for i in range(0, len(adj[u])):
            if not visited[i] and adj[u][i] > 0:
                for m in disks:
                    if m[0] >= adj[u][i]:
                        adj[u][i] = adj[u][i] - m[0]
                        adj[i][u] = adj[i][u] - m[0]
                        total_cost = total_cost + m[1]
                        find_all_paths2(adj, i, d, visited, path, all_paths, disks, total_cost)

    print(adj, total_cost)
    path.pop()
    visited[u] = False


def main():
    adjacency_matrix, disks = input_reader()
    visited = [False] * (1 + len(adjacency_matrix[0]))
    print(adjacency_matrix)
    all_paths = []
    find_all_paths2(adjacency_matrix, 0, len(adjacency_matrix[0]) - 1, visited, [], all_paths, disks, 0)
    path = [0, 1, 2, 3, 4, 5]

    # for path in all_paths:
    #     lower_disk_cost(path, adjacency_matrix, disks)


main()
