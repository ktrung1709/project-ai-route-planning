import json

real_distance_filename = 'C:\\Users\\Trung\\OneDrive - Hanoi University of Science and Technology\\Documents\\A.I\\Project-AI\\InputData\\kc_ke.json'
heuristics_distance_filename = 'C:\\Users\\Trung\\OneDrive - Hanoi University of Science and Technology\\Documents\\A.I\\Project-AI\\InputData\\crow_flies.json'
def read_from_json_file(filename):
    f = open(filename)
    data = json.load(f)
    for city in data:
        for neighbor in data[city]:
            data[city][neighbor] = float(data[city][neighbor])
    return data

# Real distance between two cities
city_map = read_from_json_file(real_distance_filename)
    # Heuristic distance between two cities
heuristics_distance = read_from_json_file(heuristics_distance_filename)