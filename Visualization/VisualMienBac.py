from operator import index
from turtle import color
import matplotlib.pyplot as plt
import networkx as nx

DuongDi = ['HaNoi', 'BacNinh', 'HaiDuong', 'HungYen', 'HaNam']
import csv
with open('C:/Users/LENOVO/Desktop/ProjectAI/Data/north_cities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_reader = list(csv_reader)
    line_count = 0
    for row in csv_reader:
        line_count += 1
#generate data for city nodes
pos = {}
for i in range(1,len(csv_reader)):
    location = csv_reader[i][1]
    pos[location] = (float(csv_reader[i][3]), float(csv_reader[i][2]))
with open('C:/Users/LENOVO/Desktop/ProjectAI/Data/Kc_ke.csv') as csv_file:
    kcke_reader = csv.reader(csv_file, delimiter = ',')
    kcke_reader = list(kcke_reader)
    line_count = 0
    for row in kcke_reader:
        line_count += 1
for i in range(1,len(kcke_reader)):
    if kcke_reader[i] == ['', '.', '']:
        continue
#generate data edges
khoang_cach = []
for i in range(1,len(kcke_reader)):
    if kcke_reader[i] == ['', '.', '']:
        continue
    khoang_cach.append(list((kcke_reader[i][0], kcke_reader[i][1], kcke_reader[i][2])))
G = nx.Graph()
#generate city nodes
for key in list(pos.keys()):
    G.add_node(key, pos = pos[key])
#generate edges
for edge in khoang_cach:
    for i in pos.keys():
        #generate colors
        if i in DuongDi and DuongDi.index(i) < len(DuongDi) - 1:
            G.add_edge(DuongDi[DuongDi.index(i)],DuongDi[DuongDi.index(i) + 1], color = 'r')
        else:
            G.add_edge(edge[0], edge[1], color = 'black', weight = edge[2])


#apply colors
colors = nx.get_edge_attributes(G,'color').values()
#draw
from matplotlib import transforms
plt.figure(3,figsize=(10,10)) 
nx.draw(G, pos = pos, edge_color = colors, with_labels = True)
plt.show()  
# print(pos.keys())