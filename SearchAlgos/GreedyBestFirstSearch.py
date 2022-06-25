import heapdict
import sys
sys.path.append(str(sys.path[0]) + '\\Visualization')
from VisualMienBac import printMap

def GBFS(start_city, end_city, city_map, heuristics_distance):
    if start_city not in heuristics_distance.keys():
        print('Can not find the start city. Please select a start city again.')
        return
    elif end_city not in heuristics_distance.keys():
        print('Can not find the end city. Please select an end city again.')
        return
    if start_city == end_city:
        print('Total distance: 0')
        print('Best route: ')
        return

    cur_city = start_city
    time_space = 1
    visited = {start_city: None}

    hd = heapdict.heapdict()

    while cur_city != end_city:
        for neighbor_city in city_map[cur_city].keys():
            if neighbor_city not in visited.keys():
                # Kiểm tra có heuristic cho city đó không
                if neighbor_city in heuristics_distance.keys() \
                        and end_city in heuristics_distance[neighbor_city].keys():
                    hd[f"{neighbor_city}@{cur_city}"] = heuristics_distance[neighbor_city][end_city]
                    time_space += 1

        try:
            next_city, visited[next_city] = hd.popitem()[0].split("@")
        except KeyError and IndexError:
            print("The algorithm can not return a solution!")
            return

        cur_city = next_city

    shortest_path, total_distance = trace_back(visited, end_city, city_map)

    print(f"Time complexity: {time_space}")
    print(f"Space complexity: {time_space}")
    print(f'Total distance: {total_distance}')
    print(f'Shortest path: {shortest_path}')

    printMap(shortest_path)


def trace_back(visited: dict, end_city, city_map):

    path = []
    total_distance = 0
    cur_city = end_city
    cur_city_parent = visited[end_city]
    while 1:
        if cur_city_parent is not None:
            path.append(cur_city)
            total_distance += city_map[cur_city_parent][cur_city]
            cur_city = visited[cur_city]
            cur_city_parent = visited[cur_city]
        else:
            path.append(cur_city)
            break
    path.reverse()
    return path, total_distance 