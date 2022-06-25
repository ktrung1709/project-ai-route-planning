import queue as Q
import sys
sys.path.append(str(sys.path[0]) + '\\Visualization')

from VisualMienBac import printMap

def UCS(start_city, end_city, city_map):
    
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

    time_space = 1
    cur_city = start_city
    queue = Q.PriorityQueue()
    cities_list = [start_city]
    cost = 0
    visited = [start_city]

    # Initial queue
    queue.put((0, cities_list))

    while not queue.empty():

        for neighbor in city_map[cur_city]:
            if neighbor not in visited:
                temp = cities_list[:]
                temp.append(neighbor)
                time_space = time_space + 1
                queue.put((cost + city_map[cur_city][neighbor], temp))
        # Pop the top priority item out of the PriorityQueue
        node = queue.get()
        # Get the cost, cities_list and last_city
        cost = node[0]
        cities_list = node[1]
        last_city = cities_list[len(cities_list) - 1]

        if end_city == last_city:
            break
        
        visited.append(last_city)
        cur_city = last_city

    print("Time complexity: " + str(time_space))
    print("Space complexity: " + str(time_space))
    print("Path found: " + str(cities_list))
    print("Cost = " + str(cost))
    printMap(cities_list)
