import heapdict

def GBFS(start_city, end_city, city_map, heuristics_distance):
    if(start_city not in heuristics_distance.keys()):
        print('Can not find the start city. Please select a start city again.')
        return
    elif(end_city not in heuristics_distance.keys()):
        print('Can not find the end city. Please select an end city again.')
        return
    if(start_city == end_city):
        print('Total distance: 0')
        print('Best route: ')
        return
 
    total_distance = 0
    cur_city = start_city
    time_space = 1
    visited = [start_city]

    hd = heapdict.heapdict()
    heuristics_table = []

    for city in heuristics_distance.keys():
        heuristics_table.append((city, (int(heuristics_distance[city][end_city]))))
    
    # for pair in heuristics_table:
    #     hd[pair[0]] = pair[1]

    while cur_city != end_city:
        for neighbor_city in city_map[cur_city].keys():
            if neighbor_city not in visited:
                hd[neighbor_city] = heuristics_distance[neighbor_city][end_city]
                time_space += 1
        try:
            next_city = hd.popitem()[0]
        except KeyError:
            print("The algorithm can not return a solution!")
            return

        visited.append(next_city)
        total_distance += city_map[cur_city][next_city]
        cur_city = next_city
    
    print(f"Time complexity: {time_space}")
    print(f"Space complexity: {time_space}")
    print(f'Total distance: {total_distance}')
    print(f'Path found: {visited}')   