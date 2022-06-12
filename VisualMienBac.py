import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
""" cities = pd.read_csv('C:/Users/LENOVO/Desktop/ProjectAI/Data/north_cities.csv')
#print(cities)
lat = cities['latd']
lon = cities['longd']
#print(lat)
#print(lon)
plt.plot(lat, lon)
plt.show()
kc_ke = pd.read_csv('C:/Users/LENOVO/Desktop/ProjectAI/Data/Kc_ke.csv') """
""" class GraphVisualization:
    def __init__(self):        
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)        
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

G = GraphVisualization()
G.visualize() """

import csv

with open('C:/Users/LENOVO/Desktop/ProjectAI/Data/north_cities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_reader = list(csv_reader)
    line_count = 0
    for row in csv_reader:
        #print(row)
        line_count += 1
    #print(f'Processed {line_count} lines.')
pos = {}
for i in range(1,len(csv_reader)):
    location = csv_reader[i][1]
    pos[location] = (float(csv_reader[i][2]), float(csv_reader[i][3]))
#print(pos)
with open('C:/Users/LENOVO/Desktop/ProjectAI/Data/Kc_ke.csv') as csv_file:
    kcke_reader = csv.reader(csv_file, delimiter=',')
    kcke_reader = list(kcke_reader)
    line_count = 0
    for row in kcke_reader:
        #print(row)
        line_count += 1
    #print(f'Processed {line_count} lines.')
for i in range(1,len(kcke_reader)):
    if kcke_reader[i] == ['', '.', '']:
        continue
    #print(kcke_reader[i])  
khoang_cach = []
for i in range(1,len(kcke_reader)):
    if kcke_reader[i] == ['', '.', '']:
        continue
    khoang_cach.append(list((kcke_reader[i][0], kcke_reader[i][1], kcke_reader[i][2])))
#print(khoang_cach)
G=nx.Graph()
for key in list(pos.keys()):
    G.add_node(key, pos = pos[key])
for edge in khoang_cach:
    G.add_edge(edge[0],edge[1], weight = edge[2])
x = []
y = []
for key in list(pos.keys()):
    x.append(pos[key][0])
    y.append(pos[key][1])
""" print(x)
print(y) """
from matplotlib import transforms
plt.figure(3,figsize=(10,10)) 
#plt.scatter(x,y)
#rot = transforms.Affine2D().rotate_deg(180)
nx.draw(G,pos = pos, with_labels = True)
plt.show()