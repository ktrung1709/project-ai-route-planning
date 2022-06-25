import csv
import matplotlib.pyplot as plt
import networkx as nx
import os
import sys

city_coordinate_file_path = os.path.join(sys.path[0] + "\\Visualization", "city_coordinate.csv")
neighbor_file_path = os.path.join(sys.path[0] + "\\Visualization", "neighbor.csv")

def printMap(path_format):

    path = []
    
    # reformat the returned path for reading
    for item in path_format:
        item_delete_space = item.replace(" ","")
        path.append(item_delete_space)
    
    # read the coordinate
    with open(city_coordinate_file_path, "r") as csv_file:
        coordinate_reader = csv.reader(csv_file, delimiter=',')
        coordinate_reader = list(coordinate_reader)
    
    # generate data for city nodes
    pos = {}
    
    for i in range(1, len(coordinate_reader)):
        location = coordinate_reader[i][1]
        pos[location] = (float(coordinate_reader[i][3]), float(coordinate_reader[i][2]))
    
    with open(neighbor_file_path, "r") as csv_file:
        neighbor_reader = csv.reader(csv_file, delimiter=',')
        neighbor_reader = list(neighbor_reader)
    
    for i in range(1, len(neighbor_reader)):
        if neighbor_reader[i] == ['', '.', '']:
            continue
    
    # generate data edges
    distance = []
    
    for i in range(1, len(neighbor_reader)):
        if neighbor_reader[i] == ['', '.', '']:
            continue
<<<<<<< HEAD
        distance.append(
            list((neighbor_reader[i][0], neighbor_reader[i][1], neighbor_reader[i][2])))
    
=======
        khoang_cach.append(list((kcke_reader[i][0], kcke_reader[i][1], kcke_reader[i][2])))

>>>>>>> 4e0c2e98fb91af5b05c27052846bb7f18310e90f
    G = nx.Graph()
    
    # generate city nodes
    for key in list(pos.keys()):
        G.add_node(key, pos=pos[key])
<<<<<<< HEAD
    
    # generate edges
    for edge in distance:
        for i in pos.keys():
            # generate colors
            if i in path and path.index(i) < len(path) - 1:
                G.add_edge(path[path.index(i)], path[path.index(i) + 1], color='r',weight = 5)
            else:
                G.add_edge(edge[0], edge[1], color='black', weight = 1)
    
=======

    # generate edges and colors
    for edge in khoang_cach:
        G.add_edge(edge[0], edge[1], color = 'black', weight = 1 )
    length = len(DuongDi)
    for i in range(length - 1):
        G.add_edge(DuongDi[i], DuongDi[i + 1], color = 'r', weight = 5)

>>>>>>> 4e0c2e98fb91af5b05c27052846bb7f18310e90f
    # apply colors
    colors = nx.get_edge_attributes(G, 'color').values()
    weights = nx.get_edge_attributes(G, 'weight').values()
    
    # draw
    plt.figure(3, figsize=(10, 10))
    nx.draw(G, pos=pos, edge_color=colors, width = list(weights), with_labels=True)
    
    # output the graph
    plt.show()