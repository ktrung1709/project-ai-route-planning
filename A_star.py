import preprocessing as pp

real_distance_filename = "C:\\Users\\DELL\\OneDrive - Hanoi University of Science and Technology\Desktop\\Study\\20212\\Intro to AI\\Project\\Kc_ke.json"
heuristics_distance_filename = 'C:\\Users\\DELL\\OneDrive - Hanoi University of Science and Technology\\Desktop\\Study\\20212\\Intro to AI\\Project\\crow_flies.json'

def printData(city_map):
    for start_city, dest_city in city_map.items():
        print("Start city: ", start_city)
        for key in dest_city:
            print(key + " : " + dest_city[key])

def A_star_algorithm(start_city, end_city, real_distance, h):
    if(start_city not in h.items()):
        print('Can not find the start city. Please select a start city again.')
        return
    elif(end_city not in h.items()):
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
    k = 1
    # find the best route and the min_distance
    while f[end_city] != min_cost_value:
        for city in real_distance[cur_city].keys():
            # Check unvisited cities
            if city not in visited:
                real_cost[city] = real_cost[cur_city] + real_distance[cur_city][city]
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
        print(f"Iteration {k}:")
        print(f'time: {time}')
        print(f"space: {space}")
        k = k + 1
        
    print(f"Time complexity: {time}")
    print(f"Space complexity: {space}")
    print(f'Total distance: {min_cost_value}')
    print(f'Best route: {best_route}')  
    


def main():
    # Real distance between two cities
    city_map = pp.read_from_json_file(real_distance_filename)
    # Heuristic distance between two cities
    heuristics_distance = pp.read_from_json_file(heuristics_distance_filename)
    start_city = input('Start city: ')
    end_city = input('End city: ') 

    start_city = ' '.join(start_city.split()).title()
    end_city = ' '.join(end_city.split()).title()
    A_star_algorithm(start_city, end_city,city_map,heuristics_distance)

if __name__ == '__main__':
    main()
