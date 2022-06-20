import queue as Q

def UCS(start_city, end_city, city_map):
    time_complexity = 0
    space_complexity = 0
    if start_city not in city_map:
        raise TypeError(str(start_city) + ' not found in graph !')
        return
    if end_city not in city_map:
        raise TypeError(str(end_city) + ' not found in graph !')
        return
    if(start_city == end_city):
        print('Total distance: 0')
        print('Best route: ')
        return

    queue = Q.PriorityQueue()
    queue.put((0, [start_city]))

    while not queue.empty():

        node = queue.get()
        current = node[1][len(node[1]) - 1]

        if end_city in node[1]:
            print("Path found: " + str(node[1]))
            print("Cost = " + str(node[0]))
            print("Time complexity: " + str(time_complexity) + " nodes")
            print("Space complexity: " + str(space_complexity) + " nodes")
            break

        cost = node[0]
        for neighbor in city_map[current]:
            time_complexity = time_complexity + 1

            temp = node[1][:]
            temp.append(neighbor)
            if len(temp) > space_complexity:
                space_complexity = len(temp)
            queue.put((cost + city_map[current][neighbor], temp))