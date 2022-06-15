import queue as Q
from time import time


def search(graph, start, end):
    time_complexity = 0
    space_complexity = 0
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return

    queue = Q.PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():

        node = queue.get()
        current = node[1][len(node[1]) - 1]

        if end in node[1]:
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            print("Time complexity: " + str(time_complexity) + " nodes")
            print("Space complexity: " + str(space_complexity) + " nodes")
            break

        cost = node[0]
        for neighbor in graph[current]:
            time_complexity = time_complexity + 1

            temp = node[1][:]
            temp.append(neighbor)
            if len(temp) > space_complexity:
                space_complexity = len(temp)
            queue.put((cost + graph[current][neighbor], temp))


def readGraph():
    lines = int(input())
    graph = {}

    for line in range(lines):
        line = input()

        tokens = line.split()
        node = tokens[0]
        graph[node] = {}

        for i in range(1, len(tokens) - 1, 2):
            # print(node, tokens[i], tokens[i + 1])
            # graph.addEdge(node, tokens[i], int(tokens[i + 1]))
            graph[node][tokens[i]] = int(tokens[i + 1])
    return graph


def main():
    graph = readGraph()
    search(graph, 'Arad', 'Bucharest')


if __name__ == "__main__":
    main()
