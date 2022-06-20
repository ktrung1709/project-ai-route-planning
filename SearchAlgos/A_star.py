def A_star_algorithm(start_city, end_city, real_distance, h):
    if(start_city not in h.keys()):
        print('Can not find the start city. Please select a start city again.')
        return
    elif(end_city not in h.keys()):
        print('Can not find the end city. Please select an end city again.')
        return
    if(start_city == end_city):
        print('Total distance: 0')
        print('Best route: ')
        return
    # initialize values 
    min_cost_value = 1e9    
    f ={end_city:1e9+1}
    best_route =[]
    candidates = [start_city]
    visited = [start_city]
    cur_city = start_city
    route = {cur_city :[cur_city]}
    real_cost = {cur_city : 0}
    f[cur_city] = h[cur_city][end_city] + real_cost[cur_city]
    time = 1
    space = len(route.items())
    # find the best route and the min_distance
    while f[end_city] != min_cost_value:
        for city in real_distance[cur_city].keys():
            # Check unvisited cities
            if city not in visited:
                temp_real_cost = real_cost[cur_city] + real_distance[cur_city][city]
                if city not in f.keys() or f[city] > temp_real_cost + h[city][end_city]: 
                    real_cost[city] = temp_real_cost
                    f[city] = real_cost[city] + h[city][end_city]
                    route[city] = route[cur_city].copy()
                    route[city].append(city)
                if city not in candidates:
                    candidates.append(city)
                    time = time + 1
        #find cur_city

        visited.append(cur_city)
        candidates.remove(cur_city)
        route.pop(cur_city)
        space = len(route.items())
        cur_city = list(f.items())[0][0]
        min_cost_value = list(f.items())[0][1]
        for city in candidates:
            if f[city] < min_cost_value:
                cur_city = city
                min_cost_value = f[city]
        best_route = route[cur_city].copy()
        
    print(f"Time complexity: {time}")
    print(f"Space complexity: {space}")
    print(f'Total distance: {min_cost_value}')
    print(f'Best route: {best_route}')   