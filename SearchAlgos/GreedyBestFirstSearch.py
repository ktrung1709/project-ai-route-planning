from pqdict import pqdict

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
    best_route =[start_city]
    cur_city = start_city
    time_space = 1
    

    while cur_city != end_city:
        for neighbor_city in city_map[cur_city].keys():
            f = pqdict({})
            f.additem(neighbor_city, heuristics_distance[neighbor_city][end_city])
            time_space += 1
        next_city = f.pop()
        best_route.append(next_city)
        total_distance += city_map[cur_city][next_city]

        cur_city = next_city
    
    print(f"Time complexity: {time_space}")
    print(f"Space complexity: {time_space}")
    print(f'Total distance: {total_distance}')
    print(f'Best route: {best_route}') 

     
    