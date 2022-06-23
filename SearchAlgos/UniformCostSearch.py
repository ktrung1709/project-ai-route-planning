import queue as Q
import sys
sys.path.append(str(sys.path[0]) + '\\Visualization')

from VisualMienBac import printMap

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
    # Initial queue
    queue.put((0, [start_city]))
 
    while not queue.empty():

        # Get path with smallest cost
        node = queue.get()
        time_complexity = time_complexity + 1
        # Get last city in path 
        current_city = node[1][len(node[1]) - 1]
        cost = node[0]

        if end_city in node[1]:
            print("Time complexity: " + str(time_complexity))
            print("Space complexity: " + str(space_complexity))
            print("Total distance = " + str(node[0]))
            print("Path found: " + str(node[1]))

            printMap(node[1])
            break

        # Get smallest cost

        for neighbor in city_map[current_city]:

            temp = node[1][:]
            temp.append(neighbor)
            if len(temp) > space_complexity:
                space_complexity = len(temp)
            queue.put((cost + city_map[current_city][neighbor], temp))