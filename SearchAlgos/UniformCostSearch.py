import queue as Q

def UCS(start, end, graph):
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
            print("Path found: " + str(node[1]))
            print("Cost = " + str(node[0]))
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