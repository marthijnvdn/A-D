def main():
    Input = input()
    N = int(Input.split(' ')[0])
    M = int(Input.split(' ')[1])
    W = int(Input.split(' ')[2])
    coordinates = []
    disks = []
    for i in range(0, N):
        next_line = input()
        coordinate = (int(next_line.split()[0]), int(next_line.split()[1]))
        coordinates.append(coordinate)
    for i in range(0, M):
        next_line = input()
        diskCost = (int(next_line.split()[0]), int(next_line.split()[1]))
        disks.append(diskCost)

    graphBuilder(coordinates, disks, W)

def buildGraph(current, coordinates, graph, disks, W):
    for coordinate in coordinates:
        for smallestDisk in disks:
            if abs(current[0] - coordinate[0]) <= (2 * smallestDisk[0]) and abs(current[1] - coordinate[1]) <= (2 * smallestDisk[0]):
                print(current[0] + (2 * smallestDisk[0]), coordinate[0])
                print(current[1] + (2 * smallestDisk[0]), coordinate[1])
                graph.append((current, coordinate, smallestDisk[1]))
                break

def graphBuilder(coordinates, disks, W):
    graph = []
    duplicates = []
    for j in range (0, len(coordinates)):
        current = coordinates[0]
        print(current)
        coordinates.remove(current)
        buildGraph(current, coordinates, graph, disks, W)
    print(graph)
    for i in range(0, len(graph) - 2):
        if graph[0][0] == graph[i+1][0] and graph[0][1] == graph[i+1][1]:
            duplicates.append(graph[i+1])

main()