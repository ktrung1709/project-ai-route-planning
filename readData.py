# Reading an excel file using Python
import xlrd
import json
# Give the location of the file
filename = "C:\\Users\\Admin\\OneDrive - Hanoi University of Science and Technology\\Documents\\A.I\\Project\\Kc_ke.xlsx"
heuristics_distance_file_name = 'C:\\Users\\Admin\\OneDrive - Hanoi University of Science and Technology\\Documents\\A.I\\Project\\sld.json'
def read_from_excel_file(filename):
    # To open Workbook
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    city_map = {}
    row = 1
    while row < sheet.nrows:
        start_city = sheet.cell_value(row,0)
        city_map[start_city] = {}
        while sheet.cell_value(row,1) != '.':
            dest_city = sheet.cell_value(row,1)
            city_map[start_city][dest_city] = sheet.cell_value(row,2)
            row +=1
        row += 1
    return city_map
def read_from_json_file(filename):
    f = open(filename)
    data = json.load(f)
    return data
def printData(city_map):
    for start_city, dest_city in city_map.items():
        print("Start city: ", start_city)
        for key in dest_city:
            print(key + " : " + dest_city[key])

def A_star_algorithm(start_city, end_city, real_distance, heuristics_distance):
    if(start_city == end_city):
        print('Total distance: 0')
        print('Best route: ')
        return
    # initialize values 
    min_cost_value = 1e9
    best_route =[]
    visited = []
    cur_city = start_city
    route = {}
    cost_value = {}
    evaluation_function ={end_city:1e9+1}
    # Create the first routes
    for city in real_distance[start_city].keys():
        route[city] = []
        route[city].append(start_city)
        cost_value[city] = real_distance[start_city][city]
    # find the best route and the min_distance
    while evaluation_function[end_city] != min_cost_value:
        for city in real_distance[cur_city].keys():
            # Check unvisited cities
            if city not in visited:
                evaluation_function[city] = cost_value[city] + heuristics_distance[city][end_city]
            # Remove the visited cities
            elif city in evaluation_function.keys():
                evaluation_function.pop(city)
        visited.append(cur_city)
        min_cost_value = evaluation_function[end_city]
        cur_city = end_city
        for city in evaluation_function.keys():
            if city not in visited and evaluation_function[city] <min_cost_value: 
                min_cost_value = evaluation_function[city]
                cur_city = city
        if cur_city != route[cur_city][-1]:
            route[cur_city].append(cur_city)
        best_route = route[cur_city].copy()
        # update route and cost_value for each city
        for city in real_distance[cur_city].keys():
            if city not in visited:
                route[city] = route[cur_city].copy()
                route[city].append(city)
                # print(route[city])
                cost_value[city] = cost_value[cur_city] + real_distance[cur_city][city]
    print(f'Total distance: {min_cost_value}')
    print('Best route: ')
    for city in best_route:
        print("%s " % city)

# Real distance between two cities
city_map =  read_from_excel_file(filename)
# Heuristic distance between two cities
heuristics_distance = read_from_json_file(heuristics_distance_file_name)
start_city = input('Start city: ')
end_city = input('End city: ') 

start_city = ' '.join(start_city.split()).title()
end_city = ' '.join(end_city.split()).title()
# convert real_distance into float value
for city in city_map:
    for neighbor in city_map[city]:
        city_map[city][neighbor] = float(city_map[city][neighbor])

A_star_algorithm(start_city, end_city,city_map,heuristics_distance)
