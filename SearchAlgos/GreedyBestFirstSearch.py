
from preprocessing import city_map
from preprocessing import heuristics_distance

from pqdict import pqdict

def GBFS(start_city, end_city, city_map, h):
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
 
    total_distance = 0
    best_route =[start_city]
    visited = [start_city]
    cur_city = start_city
    time_space = 1

    while cur_city != end_city:
        f = pqdict({})
        for neighbor_city in city_map[cur_city].keys():
            f.additem(neighbor_city, heuristics_distance[neighbor_city][end_city])
            time_space += 1
        next_city = f.pop()
        visited.append(next_city)
        best_route.append(next_city)
        total_distance += city_map[cur_city][next_city]

        cur_city = next_city
    
    print(f"Time complexity: {time_space}")
    print(f"Space complexity: {time_space}")
    print(f'Total distance: {total_distance}')
    print(f'Best route: {best_route}')  
    
        

def main():
    
    start_city = input('Start city: ')
    end_city = input('End city: ') 

    start_city = ' '.join(start_city.split()).title()
    end_city = ' '.join(end_city.split()).title()
    GBFS(start_city, end_city,city_map, heuristics_distance)

if __name__ == '__main__':
    main()